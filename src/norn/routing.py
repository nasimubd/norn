"""Deterministic-first task routing with optional typed decisions."""

from .decisions import DecisionProvider, TypedQuestion
from .models import Decision, DecisionKind, Task
from .policy import Policy


class Router:
    def __init__(self, provider: DecisionProvider | None = None, policy: Policy | None = None) -> None:
        self.provider = provider
        self.policy = policy or Policy()

    def route(self, task: Task) -> Decision:
        deterministic = self._deterministic(task.instruction)
        if deterministic is not None:
            return self.policy.gate(task, deterministic)
        if self.provider is None:
            return Decision(DecisionKind.APPROVAL, 0.0, "No decision provider is configured", source="router")
        response = self.provider.decide(
            task.instruction,
            {
                "route": TypedQuestion(
                    "choice",
                    "Which executor should handle this task?",
                    {"direct": "A deterministic local tool or API can complete it", "model": "Reasoning or code generation is required", "gui": "Visual desktop interaction is required", "approval": "The task is ambiguous or privileged"},
                )
            },
        )
        answer = response.get("answers", {}).get("route", {})
        if not isinstance(answer, dict):
            return Decision(DecisionKind.APPROVAL, 0.0, "Decision provider returned a malformed answer", source="decision-model")
        choice = answer.get("choice", "approval")
        probabilities = answer.get("probabilities", {})
        if not isinstance(probabilities, dict):
            probabilities = {}
        try:
            confidence = float(answer.get("confidence", probabilities.get(choice, 0.0)))
        except (TypeError, ValueError):
            confidence = 0.0
        kind = DecisionKind(choice) if choice in DecisionKind._value2member_map_ else DecisionKind.APPROVAL
        return self.policy.gate(task, Decision(kind, confidence, "Typed decision provider selected the route", probabilities, "decision-model"))

    @staticmethod
    def _deterministic(instruction: str) -> Decision | None:
        text = instruction.lower()
        if any(token in text for token in ("open safari", "click ", "type into", "move the mouse", "desktop")):
            return Decision(DecisionKind.GUI, 0.99, "Instruction explicitly requests desktop interaction")
        if any(token in text for token in ("format the csv", "list files", "read the file", "run the test", "check git")):
            return Decision(DecisionKind.DIRECT, 0.95, "Instruction matches a deterministic local operation")
        return None

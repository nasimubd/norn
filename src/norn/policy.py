"""Explicit autonomy and confidence policy."""

from dataclasses import dataclass

from .models import Decision, DecisionKind, Task


@dataclass(frozen=True, slots=True)
class Policy:
    minimum_route_confidence: float = 0.80
    require_approval_for_gui: bool = True
    require_approval_for_unknown: bool = True

    def gate(self, task: Task, decision: Decision) -> Decision:
        if decision.kind is DecisionKind.GUI and self.require_approval_for_gui:
            return Decision(DecisionKind.APPROVAL, decision.confidence, "GUI execution requires approval", decision.alternatives, decision.source)
        if decision.confidence < self.minimum_route_confidence:
            return Decision(DecisionKind.APPROVAL, decision.confidence, "Routing confidence is below policy threshold", decision.alternatives, decision.source)
        if decision.kind is DecisionKind.REJECT:
            return decision
        return decision

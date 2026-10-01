"""Typed decision-model interfaces and a dependency-free HTTP client."""

import json
from dataclasses import dataclass
from typing import Any, Protocol
from urllib.request import Request, urlopen


@dataclass(frozen=True, slots=True)
class TypedQuestion:
    question_type: str
    instructions: str
    criteria: dict[str, str] | list[str] | None = None


class DecisionProvider(Protocol):
    def decide(self, state: Any, questions: dict[str, TypedQuestion]) -> dict[str, Any]: ...


class HttpDecisionProvider:
    """Client for TypeSafe-compatible /v1/systemone decision endpoints."""

    def __init__(self, base_url: str, model: str = "local", timeout: float = 10.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    def decide(self, state: Any, questions: dict[str, TypedQuestion]) -> dict[str, Any]:
        payload = {
            "model": self.model,
            "state": state,
            "questions": {
                key: {
                    "type": question.question_type,
                    "instructions": question.instructions,
                    **({"criteria": question.criteria} if question.criteria is not None else {}),
                }
                for key, question in questions.items()
            },
        }
        request = Request(
            f"{self.base_url}/v1/systemone",
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request, timeout=self.timeout) as response:
            return json.loads(response.read())

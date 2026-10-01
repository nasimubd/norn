"""Stable data contracts shared by Norn components."""

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any
from uuid import uuid4


class TaskStatus(StrEnum):
    RECEIVED = "received"
    ROUTED = "routed"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    BLOCKED = "blocked"


class DecisionKind(StrEnum):
    DIRECT = "direct"
    MODEL = "model"
    GUI = "gui"
    APPROVAL = "approval"
    REJECT = "reject"


@dataclass(slots=True)
class Task:
    instruction: str
    task_id: str = field(default_factory=lambda: str(uuid4()))
    metadata: dict[str, Any] = field(default_factory=dict)
    status: TaskStatus = TaskStatus.RECEIVED


@dataclass(slots=True)
class Decision:
    kind: DecisionKind
    confidence: float
    rationale: str
    alternatives: dict[str, float] = field(default_factory=dict)
    source: str = "deterministic"

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")

    @property
    def requires_approval(self) -> bool:
        return self.kind in {DecisionKind.APPROVAL, DecisionKind.REJECT}

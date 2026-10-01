"""Task normalization and capability metadata."""

from dataclasses import dataclass, field
from typing import Any

from .models import Task


@dataclass(frozen=True, slots=True)
class TaskEnvelope:
    instruction: str
    capabilities: frozenset[str] = frozenset()
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_task(self) -> Task:
        if not self.instruction.strip():
            raise ValueError("instruction must not be empty")
        return Task(self.instruction.strip(), metadata={**self.metadata, "capabilities": sorted(self.capabilities)})


def normalize(instruction: str, *, capabilities: set[str] | None = None, metadata: dict[str, Any] | None = None) -> Task:
    return TaskEnvelope(instruction, frozenset(capabilities or set()), metadata or {}).to_task()

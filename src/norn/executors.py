"""Executor contracts. Integrations implement this protocol without importing Norn internals."""

from dataclasses import dataclass, field
from typing import Any, Protocol

from .models import Task


@dataclass(slots=True)
class ExecutionResult:
    ok: bool
    summary: str
    data: dict[str, Any] = field(default_factory=dict)


class Executor(Protocol):
    name: str

    def execute(self, task: Task) -> ExecutionResult: ...


class DryRunExecutor:
    name = "dry-run"

    def execute(self, task: Task) -> ExecutionResult:
        return ExecutionResult(True, f"Would execute: {task.instruction}", {"task_id": task.task_id})

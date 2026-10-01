"""Integration protocols used by external adapters."""

from typing import Protocol

from .executors import ExecutionResult
from .models import Task


class Verifier(Protocol):
    def verify(self, task: Task, result: ExecutionResult) -> bool: ...


class ApprovalProvider(Protocol):
    def approve(self, task: Task, reason: str) -> bool: ...

"""Small execution coordinator that keeps routing, policy, execution, and audit explicit."""

from .audit import AuditLog
from .executors import ExecutionResult
from .models import DecisionKind, Task
from .registry import ExecutorRegistry
from .routing import Router


class Coordinator:
    def __init__(self, router: Router, registry: ExecutorRegistry, audit: AuditLog | None = None) -> None:
        self.router = router
        self.registry = registry
        self.audit = audit

    def run(self, task: Task) -> ExecutionResult:
        decision = self.router.route(task)
        if self.audit:
            self.audit.record("route.selected", task_id=task.task_id, kind=decision.kind.value, confidence=decision.confidence)
        if decision.kind is not DecisionKind.DIRECT:
            return ExecutionResult(False, f"Task requires {decision.kind.value}", {"decision": decision.kind.value})
        executor = self.registry.get("dry-run")
        result = executor.execute(task)
        if self.audit:
            self.audit.record("execution.finished", task_id=task.task_id, ok=result.ok)
        return result

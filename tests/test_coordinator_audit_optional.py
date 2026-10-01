from norn.coordinator import Coordinator
from norn.executors import DryRunExecutor
from norn.models import Task
from norn.registry import ExecutorRegistry
from norn.routing import Router


def test_audit_is_optional():
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    assert Coordinator(Router(), registry).run(Task("run the test suite")).ok

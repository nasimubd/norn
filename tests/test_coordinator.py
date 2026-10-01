from norn.coordinator import Coordinator
from norn.executors import DryRunExecutor
from norn.models import Task
from norn.registry import ExecutorRegistry
from norn.routing import Router


def test_coordinator_runs_direct_task():
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    result = Coordinator(Router(), registry).run(Task("check git status"))
    assert result.ok

from norn.coordinator import Coordinator
from norn.executors import DryRunExecutor
from norn.models import Task
from norn.registry import ExecutorRegistry
from norn.routing import Router


def test_coordinator_does_not_execute_gui_route():
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    result = Coordinator(Router(), registry).run(Task("Open Safari"))
    assert not result.ok

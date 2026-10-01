from norn.coordinator import Coordinator
from norn.executors import DryRunExecutor
from norn.models import Task
from norn.registry import ExecutorRegistry
from norn.routing import Router


def test_non_direct_result_explains_boundary():
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    result = Coordinator(Router(), registry).run(Task("Open Safari"))
    assert "gui" in result.summary

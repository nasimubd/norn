from norn.executors import DryRunExecutor
from norn.health import check
from norn.registry import ExecutorRegistry


def test_health_is_ready_with_executor():
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    assert check(registry).ready

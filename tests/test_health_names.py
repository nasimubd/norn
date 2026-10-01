from norn.executors import DryRunExecutor
from norn.health import check
from norn.registry import ExecutorRegistry


def test_health_lists_executor_names():
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    assert check(registry).executors == ("dry-run",)

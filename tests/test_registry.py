from norn.executors import DryRunExecutor
from norn.registry import ExecutorRegistry


def test_registry_returns_sorted_names():
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    assert registry.names() == ("dry-run",)

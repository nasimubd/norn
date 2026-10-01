import pytest

from norn.executors import DryRunExecutor
from norn.registry import ExecutorRegistry


def test_registry_rejects_duplicate_names():
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    with pytest.raises(ValueError):
        registry.register(DryRunExecutor())

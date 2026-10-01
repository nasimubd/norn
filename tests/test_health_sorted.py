from norn.executors import DryRunExecutor
from norn.health import check
from norn.registry import ExecutorRegistry


class Other:
    name = "a"

    def execute(self, task):
        raise AssertionError


def test_health_uses_registry_order():
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    registry.register(Other())
    assert check(registry).executors == ("a", "dry-run")

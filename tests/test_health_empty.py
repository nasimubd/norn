from norn.health import check
from norn.registry import ExecutorRegistry


def test_health_is_not_ready_without_executor():
    result = check(ExecutorRegistry())
    assert not result.ready

from norn.health import check
from norn.registry import ExecutorRegistry


def test_empty_health_explains_reason():
    assert "no executors" in check(ExecutorRegistry()).reason

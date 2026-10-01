import pytest

from norn.registry import ExecutorRegistry


def test_registry_rejects_unknown_executor():
    with pytest.raises(KeyError):
        ExecutorRegistry().get("missing")

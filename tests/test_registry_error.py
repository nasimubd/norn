import pytest

from norn.registry import ExecutorRegistry


class EmptyName:
    name = ""


def test_registry_rejects_empty_name():
    with pytest.raises(ValueError):
        ExecutorRegistry().register(EmptyName())

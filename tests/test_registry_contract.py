from norn.registry import ExecutorRegistry


def test_empty_registry_is_safe():
    assert ExecutorRegistry().names() == ()

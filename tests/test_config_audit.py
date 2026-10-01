from norn.config import RuntimeConfig


def test_audit_is_enabled_by_default():
    assert RuntimeConfig().audit_enabled

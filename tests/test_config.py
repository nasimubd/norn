from norn.config import RuntimeConfig


def test_config_defaults_are_conservative():
    assert RuntimeConfig().minimum_confidence == 0.8

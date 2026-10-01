import pytest

from norn.config import RuntimeConfig


def test_config_rejects_invalid_confidence():
    with pytest.raises(ValueError):
        RuntimeConfig(minimum_confidence=2)

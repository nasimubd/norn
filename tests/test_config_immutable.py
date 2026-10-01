from dataclasses import FrozenInstanceError

import pytest

from norn.config import RuntimeConfig


def test_config_is_immutable():
    with pytest.raises(FrozenInstanceError):
        RuntimeConfig().audit_enabled = False

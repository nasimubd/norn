from dataclasses import FrozenInstanceError

import pytest

from norn.health import Health


def test_health_is_immutable():
    with pytest.raises(FrozenInstanceError):
        Health(True, (), "ok").ready = False

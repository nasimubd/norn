import pytest

from norn.routing import Router
from norn.service import route_payload


def test_service_rejects_missing_instruction():
    with pytest.raises(ValueError):
        route_payload({}, Router())

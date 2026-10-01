import pytest

from norn.routing import Router
from norn.service import route_payload


def test_service_rejects_nonstring_instruction():
    with pytest.raises(ValueError):
        route_payload({"instruction": 1}, Router())

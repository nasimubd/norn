from norn.routing import Router
from norn.service import route_payload


def test_service_returns_confidence():
    assert route_payload({"instruction": "list files"}, Router())["confidence"] == 0.95

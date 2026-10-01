from norn.routing import Router
from norn.service import route_payload


def test_service_returns_rationale():
    assert route_payload({"instruction": "list files"}, Router())["rationale"]

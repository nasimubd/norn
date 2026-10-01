from norn.routing import Router
from norn.service import route_payload


def test_service_preserves_unknown_approval():
    assert route_payload({"instruction": "write a strategy"}, Router())["kind"] == "approval"

from norn.routing import Router
from norn.service import route_payload


def test_service_accepts_capabilities():
    result = route_payload({"instruction": "list files", "capabilities": ["filesystem"]}, Router())
    assert result["kind"] == "direct"

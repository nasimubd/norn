from norn.routing import Router
from norn.service import route_payload


def test_service_routes_payload():
    result = route_payload({"instruction": "list files"}, Router())
    assert result["kind"] == "direct"

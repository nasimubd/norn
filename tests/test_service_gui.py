from norn.routing import Router
from norn.service import route_payload


def test_service_preserves_gui_approval():
    assert route_payload({"instruction": "Open Safari"}, Router())["kind"] == "approval"

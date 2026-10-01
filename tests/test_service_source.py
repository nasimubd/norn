from norn.routing import Router
from norn.service import route_payload


def test_service_reports_decision_source():
    assert route_payload({"instruction": "list files"}, Router())["source"] == "deterministic"

from norn.routing import Router
from norn.service import route_payload


def test_service_returns_unique_task_ids():
    first = route_payload({"instruction": "list files"}, Router())["task_id"]
    second = route_payload({"instruction": "list files"}, Router())["task_id"]
    assert first != second

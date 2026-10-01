from norn.routing import Router
from norn.service import route_payload


def test_service_accepts_metadata():
    result = route_payload({"instruction": "list files", "metadata": {"source": "test"}}, Router())
    assert result["task_id"]

import json

from norn.audit import AuditLog


def test_audit_preserves_custom_fields(tmp_path):
    target = tmp_path / "events.jsonl"
    AuditLog(target).record("route.selected", route="direct", confidence=0.95)
    event = json.loads(target.read_text())
    assert event["route"] == "direct"
    assert event["confidence"] == 0.95

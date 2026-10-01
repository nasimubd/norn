import json

from norn.audit import AuditLog


def test_audit_appends_jsonl(tmp_path):
    path = tmp_path / "audit.jsonl"
    AuditLog(path).record("task.received", task_id="123")
    record = json.loads(path.read_text().strip())
    assert record["event"] == "task.received"
    assert record["task_id"] == "123"

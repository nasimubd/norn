from norn.audit import AuditLog


def test_audit_supports_unicode(tmp_path):
    path = tmp_path / "audit.jsonl"
    AuditLog(path).record("task.received", label="中文")
    assert "中文" in path.read_text()

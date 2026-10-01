import json

from norn.audit import AuditLog
from norn.coordinator import Coordinator
from norn.executors import DryRunExecutor
from norn.models import Task
from norn.registry import ExecutorRegistry
from norn.routing import Router


def test_coordinator_records_route_and_execution(tmp_path):
    audit = AuditLog(tmp_path / "events.jsonl")
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    Coordinator(Router(), registry, audit).run(Task("check git status"))
    events = [json.loads(line)["event"] for line in (tmp_path / "events.jsonl").read_text().splitlines()]
    assert events == ["route.selected", "execution.finished"]

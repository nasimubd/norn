from norn.coordinator import Coordinator
from norn.executors import DryRunExecutor
from norn.models import Task
from norn.registry import ExecutorRegistry
from norn.routing import Router


class ApprovalProvider:
    def decide(self, state, questions):
        return {"answers": {"route": {"choice": "approval", "confidence": 1.0}}}


def test_coordinator_respects_provider_approval():
    registry = ExecutorRegistry()
    registry.register(DryRunExecutor())
    result = Coordinator(Router(ApprovalProvider()), registry).run(Task("complex work"))
    assert not result.ok

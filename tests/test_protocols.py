from norn.executors import ExecutionResult
from norn.models import Task
from norn.protocols import ApprovalProvider, Verifier


def test_protocols_are_importable():
    assert Verifier and ApprovalProvider
    assert ExecutionResult(True, "ok")
    assert Task("inspect")

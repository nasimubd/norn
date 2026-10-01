from norn.models import DecisionKind, Task
from norn.routing import Router


def test_direct_rules_precede_models():
    decision = Router().route(Task("run the test suite"))
    assert decision.kind is DecisionKind.DIRECT
    assert decision.confidence == 0.95


def test_gui_work_is_gated_by_default():
    decision = Router().route(Task("Open Safari and click the address bar"))
    assert decision.kind is DecisionKind.APPROVAL
    assert decision.requires_approval


def test_unknown_work_blocks_without_provider():
    decision = Router().route(Task("Prepare a launch strategy"))
    assert decision.kind is DecisionKind.APPROVAL
    assert decision.confidence == 0.0

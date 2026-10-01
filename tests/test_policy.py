from norn.models import Decision, DecisionKind, Task
from norn.policy import Policy


def test_low_confidence_is_escalated():
    decision = Policy(minimum_route_confidence=0.8).gate(Task("x"), Decision(DecisionKind.DIRECT, 0.4, "uncertain"))
    assert decision.kind is DecisionKind.APPROVAL


def test_gui_can_be_allowed_by_policy():
    decision = Policy(require_approval_for_gui=False).gate(Task("x"), Decision(DecisionKind.GUI, 0.9, "approved policy"))
    assert decision.kind is DecisionKind.GUI

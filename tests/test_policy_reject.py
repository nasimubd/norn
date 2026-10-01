from norn.models import Decision, DecisionKind, Task
from norn.policy import Policy


def test_policy_preserves_rejection():
    decision = Policy().gate(Task("x"), Decision(DecisionKind.REJECT, 1.0, "denied"))
    assert decision.kind is DecisionKind.REJECT

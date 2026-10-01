from norn.models import Decision, DecisionKind


def test_reject_is_always_an_approval_boundary():
    decision = Decision(DecisionKind.REJECT, 1.0, "policy denied")
    assert decision.requires_approval

from norn.models import DecisionKind


def test_decision_kind_values_are_stable():
    assert DecisionKind.APPROVAL.value == "approval"

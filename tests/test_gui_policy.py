from norn.models import Decision, DecisionKind, Task
from norn.policy import Policy


def test_gui_policy_does_not_depend_on_confidence_alone():
    result = Policy().gate(Task("open app"), Decision(DecisionKind.GUI, 1.0, "certain"))
    assert result.kind is DecisionKind.APPROVAL

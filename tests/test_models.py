import pytest

from norn.models import Decision, DecisionKind, Task


def test_task_gets_an_id_and_starts_received():
    task = Task("inspect the repository")
    assert task.task_id
    assert task.status.value == "received"


def test_decision_rejects_invalid_confidence():
    with pytest.raises(ValueError):
        Decision(DecisionKind.DIRECT, 1.1, "bad")

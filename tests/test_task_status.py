from norn.models import TaskStatus


def test_status_values_are_stable():
    assert TaskStatus.BLOCKED.value == "blocked"

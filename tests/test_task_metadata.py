from norn.models import Task


def test_task_metadata_is_isolated_per_instance():
    first = Task("one")
    second = Task("two")
    first.metadata["source"] = "cli"
    assert second.metadata == {}

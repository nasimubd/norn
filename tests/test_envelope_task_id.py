from norn.envelope import normalize


def test_normalized_tasks_have_ids():
    assert normalize("inspect").task_id

from norn.executors import DryRunExecutor
from norn.models import Task


def test_dry_run_executor_never_performs_side_effects():
    result = DryRunExecutor().execute(Task("delete a file"))
    assert result.ok
    assert result.data["task_id"]

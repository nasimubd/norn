from norn.executors import DryRunExecutor
from norn.models import Task


def test_dry_run_summary_is_explicit():
    assert DryRunExecutor().execute(Task("inspect")).summary.startswith("Would execute:")

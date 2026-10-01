from pathlib import Path


def test_ci_workflow_is_present():
    assert Path(".github/workflows/ci.yml").exists()

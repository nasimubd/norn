from norn.executors import ExecutionResult


def test_execution_result_defaults_data():
    assert ExecutionResult(True, "ok").data == {}

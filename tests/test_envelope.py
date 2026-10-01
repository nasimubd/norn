from norn.envelope import normalize


def test_normalize_strips_instruction_and_records_capabilities():
    task = normalize("  inspect  ", capabilities={"filesystem"})
    assert task.instruction == "inspect"
    assert task.metadata["capabilities"] == ["filesystem"]

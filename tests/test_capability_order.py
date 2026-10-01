from norn.envelope import normalize


def test_capabilities_are_deterministic():
    task = normalize("inspect", capabilities={"network", "filesystem"})
    assert task.metadata["capabilities"] == ["filesystem", "network"]

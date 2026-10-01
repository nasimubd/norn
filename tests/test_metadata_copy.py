from norn.envelope import normalize


def test_metadata_is_copied():
    source = {"origin": "cli"}
    task = normalize("inspect", metadata=source)
    source["origin"] = "changed"
    assert task.metadata["origin"] == "cli"

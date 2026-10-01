from norn.envelope import TaskEnvelope


def test_envelope_defaults_to_no_capabilities():
    assert TaskEnvelope("inspect").capabilities == frozenset()

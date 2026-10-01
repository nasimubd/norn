from norn.decisions import HttpDecisionProvider


def test_provider_normalizes_trailing_slashes():
    assert HttpDecisionProvider("http://localhost///").base_url == "http://localhost"

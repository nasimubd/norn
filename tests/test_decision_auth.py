from norn.decisions import HttpDecisionProvider


def test_provider_stores_optional_api_key():
    provider = HttpDecisionProvider("http://localhost", api_key="secret")
    assert provider.api_key == "secret"

from norn.argus import ArgusConfig


def test_argus_config_has_local_default(monkeypatch):
    monkeypatch.delenv("NORN_ARGUS_BASE_URL", raising=False)
    config = ArgusConfig.from_environment()
    assert config.base_url.endswith("/v1")

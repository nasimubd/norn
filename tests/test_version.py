from norn.version import __version__


def test_version_is_semantic():
    assert len(__version__.split(".")) == 3

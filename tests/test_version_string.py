from norn.version import __version__


def test_version_has_numeric_parts():
    assert all(part.isdigit() for part in __version__.split("."))

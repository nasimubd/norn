from pathlib import Path

from norn.version import __version__


def test_version_file_matches_runtime():
    assert Path("VERSION").read_text().strip() == __version__

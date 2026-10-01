from pathlib import Path


def test_verify_script_exists_and_is_executable():
    path = Path("scripts/verify.sh")
    assert path.exists()
    assert path.stat().st_mode & 0o111

from pathlib import Path


def test_citation_has_current_version():
    assert "version: 0.10.0" in Path("CITATION.cff").read_text()

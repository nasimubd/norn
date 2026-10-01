import pytest

from norn.envelope import normalize


def test_empty_instruction_is_rejected():
    with pytest.raises(ValueError):
        normalize("   ")

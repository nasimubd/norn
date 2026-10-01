import pytest

from norn.decisions import HttpDecisionProvider


def test_provider_rejects_nonpositive_timeout():
    with pytest.raises(ValueError):
        HttpDecisionProvider("http://localhost", timeout=0)

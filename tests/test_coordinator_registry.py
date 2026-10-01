import pytest

from norn.coordinator import Coordinator
from norn.models import Task
from norn.registry import ExecutorRegistry
from norn.routing import Router


def test_coordinator_reports_missing_direct_executor():
    with pytest.raises(KeyError):
        Coordinator(Router(), ExecutorRegistry()).run(Task("check git status"))

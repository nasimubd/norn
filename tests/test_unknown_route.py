from norn.models import DecisionKind, Task
from norn.routing import Router


def test_unknown_route_is_not_guessed():
    result = Router().route(Task("invent a new product strategy"))
    assert result.kind is DecisionKind.APPROVAL

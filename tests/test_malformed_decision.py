from norn.models import DecisionKind, Task
from norn.routing import Router


class MalformedProvider:
    def decide(self, state, questions):
        return {"answers": {"route": None}}


def test_malformed_answer_escalates():
    decision = Router(provider=MalformedProvider()).route(Task("ambiguous work"))
    assert decision.kind is DecisionKind.APPROVAL

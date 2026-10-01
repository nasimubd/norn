from norn.models import DecisionKind, Task
from norn.routing import Router


class BadProbabilityProvider:
    def decide(self, state, questions):
        return {"answers": {"route": {"choice": "direct", "confidence": "not-a-number", "probabilities": []}}}


def test_bad_probability_escalates():
    decision = Router(provider=BadProbabilityProvider()).route(Task("ambiguous work"))
    assert decision.kind is DecisionKind.APPROVAL
    assert decision.confidence == 0.0

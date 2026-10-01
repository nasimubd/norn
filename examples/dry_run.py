from norn.models import Task
from norn.routing import Router


task = Task("check git status")
decision = Router().route(task)
print(decision.kind.value, decision.confidence, decision.rationale)

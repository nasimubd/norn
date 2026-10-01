from norn.decisions import HttpDecisionProvider
from norn.models import Task
from norn.routing import Router


provider = HttpDecisionProvider("http://127.0.0.1:11435", model="decider-2b")
decision = Router(provider=provider).route(Task("prepare a project summary"))
print(decision)

"""Dependency-free request boundary for host adapters."""

from typing import Any

from .envelope import normalize
from .models import Decision
from .routing import Router


def route_payload(payload: dict[str, Any], router: Router) -> dict[str, Any]:
    instruction = payload.get("instruction")
    if not isinstance(instruction, str):
        raise TypeError("instruction must be a string")
    task = normalize(instruction, capabilities=set(payload.get("capabilities", [])), metadata=payload.get("metadata"))
    decision: Decision = router.route(task)
    return {"task_id": task.task_id, "kind": decision.kind.value, "confidence": decision.confidence, "rationale": decision.rationale, "source": decision.source}

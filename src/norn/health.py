"""Non-invasive runtime health summaries."""

from dataclasses import dataclass

from .registry import ExecutorRegistry


@dataclass(frozen=True, slots=True)
class Health:
    ready: bool
    executors: tuple[str, ...]
    reason: str


def check(registry: ExecutorRegistry) -> Health:
    names = registry.names()
    if not names:
        return Health(False, names, "no executors registered")
    return Health(True, names, "runtime has registered executors")

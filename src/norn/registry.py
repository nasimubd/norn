"""Allow-listed executor registry."""

from .executors import Executor


class ExecutorRegistry:
    def __init__(self) -> None:
        self._executors: dict[str, Executor] = {}

    def register(self, executor: Executor) -> None:
        if not executor.name or executor.name in self._executors:
            raise ValueError("executor name must be unique and non-empty")
        self._executors[executor.name] = executor

    def get(self, name: str) -> Executor:
        try:
            return self._executors[name]
        except KeyError as exc:
            raise KeyError(f"executor is not registered: {name}") from exc

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._executors))

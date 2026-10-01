# API contracts

The Python interfaces under `src/norn` are intentionally small. Integrations should depend on `Task`, `Decision`, `ExecutionResult`, `Router`, and the executor protocol rather than internal modules.

The future service boundary will accept a task envelope and return a decision envelope before execution. Any HTTP service must preserve the same approval and audit semantics as the in-process runtime.

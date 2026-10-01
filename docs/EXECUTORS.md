# Executors

An executor is an adapter with a name and an `execute(Task) -> ExecutionResult` method. Executors should be narrow, allow-listed, observable, and independently verifiable.

The runtime does not ship an unrestricted shell executor. A future direct executor should expose a constrained command catalog rather than evaluate model-generated code.

# Norn runtime foundation

## Summary

This change establishes Norn as a separate, local-first execution runtime above Argus. It defines the stable boundaries needed to route natural-language tasks without coupling account management, model providers, desktop automation, or policy to one implementation.

## Included

- Task, decision, status, and result data contracts.
- Deterministic-first routing with explicit approval escalation.
- TypeSafe-compatible typed decision-provider HTTP client.
- Argus endpoint configuration without credential ownership.
- Executor and verifier protocols plus a safe dry-run executor.
- Append-only JSONL audit records.
- CLI dry-run routing command.
- Architecture, operations, security, and release documentation.
- Contract tests and examples.

## Safety properties

GUI routes are approval-gated by default. Unknown work blocks when no decision provider is configured. Low-confidence decisions escalate. The runtime never evaluates model-generated shell or Python code in the core package.

## Validation

```text
21 passed
ruff check .: passed
python3 -m compileall: passed
git diff --check: passed
```

## Follow-up

Provider-specific model routing, constrained direct executors, Agent-S integration, and service packaging should land as separate adapters after this contract is reviewed.

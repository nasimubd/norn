# Norn architecture

Norn is the execution layer, not the model gateway. It receives a task, selects the smallest suitable executor, enforces a policy, and records what happened.

## Boundaries

### Argus

Argus owns provider accounts, sessions, model routing, quotas, and the OpenAI-compatible gateway. Norn only consumes a configured endpoint; it must never manage provider credentials directly.

### Decision provider

The decision provider answers typed questions. It should be local where possible and return probabilities for every allowed option. Norn treats probabilities as routing evidence, not permission to perform privileged actions.

### Executors

Executors are replaceable adapters. A direct executor can call a repository tool or API. A model executor can call an Argus-routed model. A GUI executor can wrap Agent-S. Every executor returns a structured result and must be paired with verification for side effects.

### Policy

Policy is intentionally outside the model. It defines minimum confidence, approval requirements, allowed capabilities, and whether a task can run unattended. A model cannot disable policy by returning a different answer.

## Decision lifecycle

1. Normalize the instruction into a task envelope.
2. Apply deterministic route rules.
3. Ask the local decision provider only when rules are insufficient.
4. Convert the answer into a typed decision.
5. Apply the policy gate.
6. Execute only through an allow-listed executor.
7. Verify the result.
8. Append an audit record.

## Failure handling

Unavailable decision providers, low confidence, malformed responses, and failed verification all produce a blocked task. Norn does not silently fall back from a failed safety decision to unrestricted execution.

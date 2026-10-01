# Operations

## Environment

Norn does not require a provider key for deterministic routing. Configure a local typed-decision endpoint when you want model-assisted routing:

```bash
export NORN_DECISION_BASE_URL=http://127.0.0.1:11435
export NORN_DECISION_MODEL=decider-2b
```

Configure Argus only for executors that need a larger model:

```bash
export NORN_ARGUS_BASE_URL=http://127.0.0.1:8080/v1
export NORN_ARGUS_MODEL=default
```

Keep all account login and credential storage inside Argus. Do not put secrets in `NORN_*` task metadata or audit records.

## Desktop permissions

Agent-S requires screen-recording and accessibility permissions on macOS and equivalent input permissions on other platforms. Grant them only to the process that owns the GUI executor. Keep GUI approval enabled during initial rollout.

## Rollout stages

1. Dry-run routing with deterministic rules.
2. Add a local decision model and measure confidence calibration.
3. Enable direct executors with verification.
4. Enable Argus-routed reasoning tasks.
5. Enable Agent-S for explicitly approved GUI tasks.

## Incident response

Stop the executor process, preserve the JSONL audit file, and revoke the affected Argus session. Do not delete logs before determining whether a task crossed a policy boundary.

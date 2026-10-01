# Auditing

The JSONL audit format is append-only and records event time, event type, and task identifiers. Do not include task text or credentials unless the deployment has an explicit data-retention policy.

Production deployments should rotate audit files, restrict permissions, and ship records to an append-only store.

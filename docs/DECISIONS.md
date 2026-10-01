# Architecture decisions

## Runtime is separate from Argus

Argus is already a high-throughput gateway. Norn must not duplicate account management, provider adapters, or gateway concerns.

## Decision models are gates, not authorities

Typed probabilities are useful for fast routing and escalation. They do not replace deterministic policy or verification.

## Upstream runtimes remain external

Agent-S and decision-model implementations are runtime dependencies or adapters. Norn does not vendor their source or weights.

## Local-first is an optimization, not a trust boundary

Local inference can reduce cost and latency, but local model output receives the same policy treatment as hosted output.

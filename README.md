# Norn

Norn is a local-first agent runtime for routing natural-language tasks across deterministic tools, local decision models, Argus-routed models, desktop automation, and human approval.

The name comes from Norse mythology: the Norns are the beings who shape the course of events. Norn applies that idea to software by deciding which executor should handle a request, how much autonomy is appropriate, and when a task must be verified or handed back to a person. It is pronounced **“norn”**.

Norn is not a model provider and does not replace Argus. Argus remains the high-throughput gateway and account/session proxy; Norn is the optional execution and policy layer above it.

## Design goals

- Prefer deterministic tools and direct APIs over model calls.
- Use a local typed-decision model for fast routing and safety gates.
- Send reasoning and vision work through configured Argus-compatible endpoints.
- Invoke Agent-S only when a task genuinely requires desktop interaction.
- Abstain and request approval when confidence, permissions, or verification are insufficient.
- Keep credentials, model weights, and user data outside the repository.

## Status

Norn is an initial runtime foundation. The stable interfaces are the task envelope, router, policy gate, executor protocol, and audit record. Provider adapters and desktop execution are deliberately optional.

## Quick start

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e '.[dev]'
norn --help
```

Run a dry routing decision without a model:

```bash
norn route 'Format the CSV files in ./data and report the result'
```

Run the test suite:

```bash
pytest
```

## Runtime flow

```text
request -> normalize -> deterministic checks -> decision model -> policy gate
                                      |                  |
                         direct/tool executor      Argus / Agent-S / approval
                                      \__________________/
                                            verify -> audit
```

## Repository layout

```text
src/norn/
  audit.py       durable JSONL audit records
  cli.py         command-line entry point
  decisions.py   typed decision model protocol and HTTP client
  executors.py   executor contracts and built-in dry-run executor
  models.py      task and decision data structures
  policy.py      confidence and approval gates
  routing.py     deterministic-first routing engine
  argus.py       OpenAI-compatible Argus client configuration
tests/           contract and behavior tests
docs/            architecture and operator documentation
```

## Security

Norn is designed to make privileged execution explicit. Desktop automation and local code execution are disabled unless an executor and policy allow them. Do not expose an executor endpoint to untrusted callers, and do not put provider credentials in task text, logs, or Git.

## License

Apache-2.0. See [LICENSE](LICENSE).

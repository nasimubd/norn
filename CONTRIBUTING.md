# Contributing

Keep changes small, testable, and scoped to one boundary. Add or update contract tests whenever a public interface changes.

Use Conventional Commits. Do not include credentials, model weights, private task data, generated logs, or attribution trailers that do not describe the actual authorship of a change.

Before opening a pull request:

```bash
ruff check .
pytest
git diff --check
```

Document new executors in `docs/ARCHITECTURE.md` and make their permission requirements explicit.

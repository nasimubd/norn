#!/usr/bin/env bash
set -euo pipefail

python3 -m compileall -q src
if [[ -x .venv/bin/pytest ]]; then
  .venv/bin/pytest -q
  .venv/bin/ruff check .
else
  echo "development environment missing; install with: python3 -m venv .venv && .venv/bin/pip install -e '.[dev]'" >&2
  exit 1
fi
./mise-tasks/release/check
test "$(cat VERSION)" = "$(sed -n 's/^version = "\(.*\)"$/\1/p' pyproject.toml)"
test "$(cat VERSION)" = "$(PYTHONPATH=src .venv/bin/python -c 'from norn.version import __version__; print(__version__)')"
echo "Norn end-to-end verification passed"

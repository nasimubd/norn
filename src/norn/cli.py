"""Command-line interface for Norn."""

import argparse
import json
import sys

from .models import Task
from .executors import DryRunExecutor
from .health import check
from .registry import ExecutorRegistry
from .routing import Router


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="norn", description="Route natural-language tasks across safe executors.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    route = subparsers.add_parser("route", help="show the selected route without executing it")
    route.add_argument("instruction")
    route.add_argument("--json", action="store_true", help="emit machine-readable output")
    subparsers.add_parser("health", help="show non-invasive local readiness")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "route":
        task = Task(args.instruction)
        decision = Router().route(task)
        payload = {"task_id": task.task_id, "kind": decision.kind.value, "confidence": decision.confidence, "rationale": decision.rationale}
        if args.json:
            print(json.dumps(payload, sort_keys=True))
        else:
            print(f"{decision.kind.value} ({decision.confidence:.0%}): {decision.rationale}")
        return 0
    if args.command == "health":
        registry = ExecutorRegistry()
        registry.register(DryRunExecutor())
        result = check(registry)
        print(json.dumps({"ready": result.ready, "executors": result.executors, "reason": result.reason}, sort_keys=True))
        return 0 if result.ready else 1
    return 2


if __name__ == "__main__":
    sys.exit(main())

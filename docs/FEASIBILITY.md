# NORN and Agent-S feasibility assessment

## Verified state

NORN is a dependency-free Python routing, policy, executor, and audit layer. The repository does not contain Agent-S, model weights, a local inference server, a desktop executor, a shell executor, or an operating-system kernel. Its current coordinator executes only the built-in dry-run executor; GUI decisions remain blocked until a separately registered approval-aware GUI adapter exists.

On the inspected development laptop, Argus 1.27.4 is installed and a local `argus serve` process is listening on `127.0.0.1:8080`. That proves the gateway is available, not that every requested model route is configured. NORN can be pointed at an OpenAI-compatible Argus endpoint, but this does not install Agent-S or implement the missing NORN GUI adapter.

Agent-S is a separate open-source computer-use framework. Its README describes support for macOS, Windows, and Linux, but it still runs as a user-space application and requires the host operating system, display server, input APIs, permissions, Python dependencies, and one or more model endpoints.

## Feasible now

- Run deterministic NORN routing and dry-run execution locally.
- Configure NORN to call an available Argus-compatible endpoint for model-backed adapters once an adapter is implemented.
- Install Agent-S separately and run it as an explicitly approved GUI executor.
- Use Agent-S on macOS, Windows, or Linux with the platform-specific accessibility and input permissions it requires.
- Keep model inference remote through Argus or another provider to limit local memory use.

## Not provided by this repository

- A turnkey NORN plus Agent-S installation.
- A registered Agent-S executor in NORN.
- A general unrestricted shell or code executor.
- A replacement kernel, filesystem, driver stack, window manager, or boot environment.
- Evidence that a local Argus endpoint exposes a particular model or that Agent-S can use it without configuration.

## Operating-system boundary

Even the complete NORN plus Argus plus Agent-S stack would be an agent layer running on macOS, Windows, or Linux. Agent-S can observe and control a desktop through screenshots, keyboard, and mouse actions; it cannot replace the host operating system. A practical deployment is:

```text
host operating system -> Argus gateway + Agent-S -> NORN policy, routing, approval, and audit
```

## Safety boundary

Agent-S documentation warns that its local coding environment can execute arbitrary Python and Bash with the invoking user's permissions. Keep that feature disabled unless the task is trusted and the process is sandboxed. Keep NORN approval and verification enabled for GUI side effects.

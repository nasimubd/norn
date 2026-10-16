# Agentic stack benchmarks and expansion plan

## NORN baseline measurements

Measurements were collected on an Apple Silicon macOS laptop with 8 CPU cores, 16 GiB RAM, and Python 3.14.7. No package installation or repository mutation was required.

| Workload | Wall time | Peak resident memory |
| --- | ---: | ---: |
| `norn health` | ~0.07 s | ~24.3 MiB |
| deterministic `norn route` | ~0.07 s | ~24.5 MiB |
| GUI approval route | ~0.06 s | ~24.4 MiB |
| 100,000 in-process deterministic routes | 0.32 s | ~23.5 MiB |

The repository occupies approximately 1.5 MB. The core has no required third-party runtime dependencies. The development test suite was not run because `pytest` was absent; it was not installed for this measurement.

## Argus observation

Argus 1.27.4 is installed on the measured host. A resident `argus serve` process listens on `127.0.0.1:8080`; its observed RSS was approximately 27 MB. An associated `argus-watch` process used approximately 74 MB RSS. These figures exclude the memory used by any remote model service and do not establish that every model endpoint is configured.

## Agent-S repository investigation

The referenced Agent-S repository was cloned into a temporary directory and removed after inspection. Its current README describes Agent S3 as a computer-use framework for macOS, Windows, and Linux. The documented installation pulls a separate Python package (`gui-agents`) and also calls for Tesseract. The requirements include computer-vision, OCR, browser/UI automation, numerical, API, and platform-specific packages such as `paddlepaddle`, `paddleocr`, `pyautogui`, `pytesseract`, `openai`, and `anthropic`.

The README recommends a hosted main model and a grounding model such as UI-TARS-1.5-7B. A local installation therefore has two materially different profiles:

- Remote inference: local Agent-S client and dependencies, with model memory and most inference compute remote.
- Local inference: Agent-S plus the chosen vision/action model, whose memory and CPU/GPU cost depends on model size, quantization, context, and screenshot rate.

Agent-S documentation warns that its optional local coding environment executes arbitrary Python and Bash with the user's permissions. It should remain disabled or sandboxed for untrusted tasks.

## Benchmark naming and results

The Agent-S repository reports **OSWorld**, **WindowsAgentArena**, and **AndroidWorld** results. It does not present a benchmark named “AgentWorld.” The README reports these results for its cited Agent S3 configurations:

- OSWorld: 66% for Agent S3 alone in the 100-step setting; 72.6% with Behavior Best-of-N.
- WindowsAgentArena: 50.2% for Agent S3 alone; 56.6% with selection from three rollouts.
- AndroidWorld: 68.1% alone; 71.6% with selection from three rollouts.

These are benchmark claims from the upstream project, not measurements performed on this laptop. They measure task success in particular environments; they do not show that Agent-S replaces an operating system.

## Empirical limits

A full GUI benchmark was not run locally because Agent-S, its dependencies, model endpoints, and required macOS accessibility/screen-recording permissions are not installed or configured. Running it would also require selecting tasks and granting an agent permission to control the desktop. The measured NORN and Argus numbers therefore should not be extrapolated as the resource cost of Agent-S inference.

A responsible full-stack benchmark should record idle and active RSS, CPU utilization, GPU utilization and memory, screenshot/action rate, latency, task success, API/token cost, and failure or approval rates. It should run in a disposable desktop session with a fixed task set and no access to sensitive data.

## Plan toward a broader agentic stack

1. Define an explicit Agent-S executor protocol in NORN, including approval, capability allow-lists, cancellation, timeout, verification, and audit events.
2. Implement an Agent-S adapter that passes only approved task envelopes and translates results into NORN execution results.
3. Add provider health checks for Argus and grounding/model endpoints without treating connectivity as model readiness.
4. Run deterministic, remote-model, and local-model benchmarks separately.
5. Add a sandboxed desktop test environment and reproducible OSWorld-style task harness.
6. Measure resource and reliability budgets before enabling unattended execution.
7. Keep the host OS boundary explicit: the result is an agent layer over macOS, Windows, or Linux, not a replacement kernel or desktop operating system.

# Citation guide

Norn is a small orchestration layer. Its behavior depends on the selected host, gateway, decision model, and executor, so cite the runtime components that were actually used in an experiment.

## Runtime integrations

| Component | Role | Source |
|---|---|---|
| Argus | Account-aware model gateway | [nasimubd/homebrew-argus](https://github.com/nasimubd/homebrew-argus) |
| Agent-S | Optional desktop executor | [simular-ai/Agent-S](https://github.com/simular-ai/Agent-S) |
| Decider | Typed decision model | [Mapika/decider](https://github.com/Mapika/decider) |
| Von | Lightweight typed decision model | [wfzyx/von](https://github.com/wfzyx/von) |
| Ollaya | Local decision serving | [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya) |
| Laya | Open typed-decision weights | [Hugging Face](https://huggingface.co/convaiinnovations/laya) |

## Project author

```bibtex
@software{nasim_norn,
  author = {MD NASIM},
  title = {Norn: A local-first agent runtime},
  year = {2026},
  url = {https://github.com/nasimubd/norn}
}
```

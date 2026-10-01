"""Configuration for routing model calls through an Argus-compatible endpoint."""

import os
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ArgusConfig:
    base_url: str
    model: str
    api_key: str | None = None

    @classmethod
    def from_environment(cls) -> "ArgusConfig":
        base_url = os.environ.get("NORN_ARGUS_BASE_URL", "http://127.0.0.1:11434/v1")
        model = os.environ.get("NORN_ARGUS_MODEL", "default")
        return cls(base_url, model, os.environ.get("NORN_ARGUS_API_KEY"))

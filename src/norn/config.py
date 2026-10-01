"""Environment-free configuration values for deployment boundaries."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RuntimeConfig:
    minimum_confidence: float = 0.80
    audit_enabled: bool = True

    def __post_init__(self) -> None:
        if not 0.0 <= self.minimum_confidence <= 1.0:
            raise ValueError("minimum_confidence must be between 0 and 1")

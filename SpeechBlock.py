from dataclasses import dataclass, field

__all__ = [
    "SpeechBlock"
]


@dataclass
class SpeechBlock:
    speaker: int = 0
    statements: list[str] = field(default_factory=list)

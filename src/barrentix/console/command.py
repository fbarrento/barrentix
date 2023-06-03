from dataclasses import dataclass, field
from typing import List
from barrentix.contracts.console import AbstractCommand


@dataclass
class Command(AbstractCommand):
    argv: List[str] = field(default_factory=lambda: [])

    def __post_init__(self) -> None:
        self.arguments()

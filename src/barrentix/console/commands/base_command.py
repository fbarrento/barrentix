from dataclasses import dataclass, field
from barrentix.contracts.console import AbstractCommand
from barrentix.console import Command
from barrentix.foundation import Application
from typing import Dict, Callable


@dataclass
class BaseCommand(Command):
    app: Application | None = field(default=None)
    commands: Dict[str, Dict[str, Callable[..., AbstractCommand]]
                   ] = field(default_factory=lambda: {})

    @property
    def signature(self) -> str:
        return "base"

    @property
    def description(self) -> str:
        return (
            "Hello from base Command"
        )

    def arguments(self) -> None:
        setattr(self, "command", None)

    def handle(self) -> None:
        if self.app is not None:
            print(f"{self.app.config.app.name}")

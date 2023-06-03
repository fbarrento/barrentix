from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, List
from pathlib import Path
from barrentix.contracts.console import AbstractConsoleKernel
from barrentix.foundation import Application


@dataclass
class ConsoleKernel(AbstractConsoleKernel):
    app: Application
    load_commands_from: List[Path] = field(default_factory=lambda: [])

    def __post_init__(self) -> None:
        self.commands()

    def load(self, path: Path) -> None:
        self.load_commands_from.append(path)

    @abstractmethod
    def commands(self) -> None:
        raise NotImplementedError

    def handle(self, args: Any) -> None:
        return super().handle(args)

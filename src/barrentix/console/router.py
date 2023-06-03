from dataclasses import dataclass
from typing import Any, Dict
from barrentix.contracts.console import AbstractConsoleRouter


@dataclass
class ConsoleRouter(AbstractConsoleRouter):
    routes: Dict[str, str]

    def handle(self, args: Any) -> None:
        return super().handle(args)

from typing import Any
from pytest import fixture
from pathlib import Path
from barrentix.foundation.container import inject
from barrentix.console.kernel import ConsoleKernel as MainConsoleKernel


@inject
class ConsoleKernel(MainConsoleKernel):

    def commands(self) -> None:
        path = Path(
            self.app.config.app.paths.tests,
            "fixtures"
            "app",
            "commands"
        )
        self.load(path)

    def handle(self, args: Any) -> None:
        return super().handle(args)


@fixture
def console_kernel() -> MainConsoleKernel:
    return ConsoleKernel()

from pytest import fixture
from barrentix.foundation.container import inject
from barrentix.console.kernel import ConsoleKernel as MainConsoleKernel


@inject
class ConsoleKernel(MainConsoleKernel):

    def commands(self) -> None:
        self.load_from_module("barrentix.console.commands")
        self.load_from_module("tests.fixtures.app.commands")


@fixture
def console_kernel() -> MainConsoleKernel:
    return ConsoleKernel()

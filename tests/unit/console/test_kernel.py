from pytest import CaptureFixture
from pytest_mock import mocker, MockerFixture  # noqa # type:ignore
from typing import Any
from barrentix.foundation import (
    Application
)
from tests.fixtures.foundation.application import app  # noqa # type:ignore
from tests.fixtures.foundation.kernel import ConsoleKernel


class TestKernel():

    def test_it_loads_commands(
        self,
        app: Application  # type:ignore # noqa
    ) -> None:

        app.singleton(
            ConsoleKernel,
            ConsoleKernel
        )

        kernel = app.make(ConsoleKernel)

        commands = kernel.get_commands()

        assert "app" in commands.keys()
        assert "base" in commands.keys()

    def test_it_resolves_a_command(
        self,
        app: Application,  # type:ignore # noqa
        mocker: MockerFixture,  # type:ignore # noqa
        capsys: CaptureFixture  # type:ignore # noqa
    ) -> None:
        mocker.patch(
            "sys.argv",
            [
                "app:test",
                "-q",
                "--port",
                "8883"
            ]
        )
        app.singleton(ConsoleKernel, ConsoleKernel)
        kernel = app.make(ConsoleKernel)
        kernel.handle()

        captured: Any = capsys.readouterr()
        assert captured.out == "Handling Test Command\n"

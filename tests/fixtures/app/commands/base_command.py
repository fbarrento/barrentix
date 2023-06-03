from barrentix.console import Command


class TestCommand(Command):

    def _arguments(self) -> None:
        self.add_argument("command")

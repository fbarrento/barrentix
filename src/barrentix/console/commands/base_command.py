from barrentix.console import Command


class BaseCommand(Command):

    def _arguments(self) -> None:
        self.add_argument("command")

    def handle(self) -> None:
        print("Handling Base Command")

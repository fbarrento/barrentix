from barrentix.console import Command


class TestCommand(Command):

    @property
    def signature(self) -> str:
        return "app:test"

    @property
    def description(self) -> str:
        return (
            "Hello from base Command"
        )

    def arguments(self) -> None:
        setattr(self, "command", None)

    def handle(self) -> None:
        print("Handling Test Command")

import sys
from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Any, List, Dict, Callable
from barrentix.contracts.console import AbstractConsoleKernel
from barrentix.foundation import Application
from barrentix.foundation.class_loader import ClassLoader
from barrentix.contracts.console import AbstractCommand


@dataclass
class ConsoleKernel(AbstractConsoleKernel, ClassLoader):
    app: Application
    base_modules: List[str] = field(default_factory=lambda: [])
    modules: Dict[str, List[str]] = field(default_factory=lambda: {})
    commands_paths: List[str] = field(default_factory=lambda: [])
    _commands: Dict[str, Dict[str, Callable[..., AbstractCommand]]
                    ] = field(default_factory=lambda: {})

    def __post_init__(self) -> None:
        self.argv = sys.argv
        self.commands()
        self.load_commands()

    def load_from_module(self, module: str) -> None:
        self.base_modules.append(module)

    def _get_modules(self, base_modules: List[str]) -> Dict[str, List[str]]:
        modules: Dict[str, List[str]] = {}
        for module in base_modules:
            modules[module] = [
                command_name for command_name
                in self._make_modules_names(module)
            ]
        return modules

    def load_commands(self) -> None:
        modules = self._get_modules(
            base_modules=self.base_modules
        )
        for module in modules:
            for command in modules[module]:
                self.load_command(
                    command=self.load(
                        module=f"{module}.{command}"
                    )
                )

    def load_command(self, command: Any) -> None:
        abstract = command
        command = command()
        group: str | List[str] = command.signature.split(":")
        if isinstance(group, list):
            group = group[0]
        self._commands[group] = {command.signature: abstract}

    def get_commands(self) -> Dict[str, Dict[str, Callable[
            ..., AbstractCommand]]]:
        return self._commands

    @abstractmethod
    def commands(self) -> None:
        raise NotImplementedError

    def handle(self) -> None:
        base_command = self._commands["base"]["base"](
            argv=self.argv,
            app=self.app,
            commands=self._commands
        )
        if len(self.argv[1:]) == 0:
            return base_command.handle()

        group = self.argv[0]
        if ":" in self.argv[0]:
            group = self.argv[0].split(":")[0]

        try:
            command = self._commands[group][self.argv[0]](self.argv)
            return command.handle()
        except KeyError:
            return base_command.handle()

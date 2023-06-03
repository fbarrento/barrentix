from abc import ABC, abstractmethod
from typing import Any


class AbstractConsoleRouter(ABC):

    @abstractmethod
    def handle(self, args: Any) -> None:
        return NotImplementedError

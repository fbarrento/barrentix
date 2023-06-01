from abc import ABC, abstractmethod
from typing import Any, Callable


class ContainerInterface(ABC):
    @abstractmethod
    def register(
        self,
        name: str | Callable[..., Any],
        dependency: Any,
    ) -> None:
        return NotImplementedError

    def resolve(self, name: str) -> Any:
        return NotImplementedError

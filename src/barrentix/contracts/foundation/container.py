from abc import ABC, abstractmethod
from typing import Any, Callable, Type


class AbstractContainer(ABC):
    @abstractmethod
    def bind(
        self,
        name: str | Callable[..., Any] | Type[Any],
        dependency: Any,
    ) -> None:
        return NotImplementedError

    @abstractmethod
    def singleton(
        self,
        name: str | Callable[..., Any] | Type[Any],
        dependency: Any
    ) -> None:
        return NotImplementedError

    def resolve(self,
                name: str | Callable[..., Any] | Type[Any]
                ) -> Any:
        return NotImplementedError

    def make(
        self,
        name: str | Callable[..., Any] | Type[Any]
    ) -> Any:
        return NotImplementedError

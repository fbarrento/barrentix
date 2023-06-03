from abc import ABC, abstractmethod, abstractproperty


class AbstractCommand(ABC):

    @abstractproperty
    def signature(self) -> str:
        raise NotImplementedError

    @abstractproperty
    def description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def arguments(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def handle(self) -> None:
        raise NotImplementedError

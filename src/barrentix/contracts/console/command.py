from abc import ABC, abstractmethod, abstractproperty


class AbstractCommand(ABC):

    @abstractmethod
    def handle(self) -> None:
        raise NotImplementedError

    @abstractproperty
    def signature(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def _description(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _arguments(self) -> None:
        raise NotImplementedError

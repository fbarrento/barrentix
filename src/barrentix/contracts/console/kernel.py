from abc import abstractmethod
from barrentix.contracts.foundation import AbstractKernel


class AbstractConsoleKernel(AbstractKernel):

    @abstractmethod
    def commands(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def load_from_module(self, module: str) -> None:
        raise NotImplementedError

from abc import abstractmethod
from barrentix.contracts.foundation import AbstractKernel


class AbstractConsoleKernel(AbstractKernel):

    @abstractmethod
    def commands(self) -> None:
        raise NotImplementedError

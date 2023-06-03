from abc import abstractmethod
from dataclasses import dataclass
from typing import Any
from barrentix.contracts.foundation import AbstractApplication
from barrentix.contracts.foundation.loader import AbstractLoader


@dataclass
class AbstractKernel(AbstractLoader):
    app: AbstractApplication

    @abstractmethod
    def handle(self) -> None:
        raise NotImplementedError

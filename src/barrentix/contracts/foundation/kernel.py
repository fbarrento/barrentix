from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any
from barrentix.contracts.foundation import AbstractApplication


@dataclass
class AbstractKernel(ABC):
    app: AbstractApplication

    @abstractmethod
    def handle(self, args: Any) -> None:
        raise NotImplementedError

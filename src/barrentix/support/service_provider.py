from abc import ABC
from dataclasses import dataclass
from omegaconf import ListConfig, DictConfig
from barrentix.contracts.foundation import AbstractContainer


@dataclass
class ServiceProvider(ABC):

    app: AbstractContainer

    config: DictConfig | ListConfig

    def boot(self) -> None:
        raise NotImplementedError

    def register(self) -> None:
        raise NotImplementedError

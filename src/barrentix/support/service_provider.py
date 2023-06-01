from abc import ABC
from dataclasses import dataclass
from omegaconf import ListConfig, DictConfig
from barrentix.contracts.foundation import ApplicationInterface


@dataclass
class ServiceProvider(ABC):

    app: ApplicationInterface

    config: DictConfig | ListConfig

    def boot(self) -> None:
        raise NotImplementedError

    def register(self) -> None:
        raise NotImplementedError

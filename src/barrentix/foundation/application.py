from dataclasses import dataclass
from typing import Type
from omegaconf import DictConfig, ListConfig
from barrentix.contracts.foundation import AbstractApplication
from barrentix.support.service_provider import ServiceProvider
from barrentix.foundation import Container
from importlib import import_module


@dataclass
class Application(AbstractApplication, Container):

    config: DictConfig | ListConfig

    def __post_init__(self) -> None:
        self.singleton(
            name=Application,
            dependency=self
        )

    def boot(self) -> None:
        self.register_service_providers()

    def register_service_providers(self) -> None:
        providers = self.config.app.service_providers
        for provider_module in providers:
            module = import_module(provider_module)
            provider: Type[ServiceProvider] = getattr(
                module, providers[provider_module])

            service_provider = provider(
                app=self,
                config=self.config
            )
            service_provider.register()

    def boot_service_providers(self) -> None:
        return super().boot_service_providers()

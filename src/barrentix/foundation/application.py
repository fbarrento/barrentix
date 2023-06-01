from dataclasses import dataclass
from omegaconf import DictConfig, ListConfig
from barrentix.contracts.foundation.application import ApplicationInterface
from barrentix.support.service_provider import ServiceProvider
from importlib import import_module


@dataclass
class Application(ApplicationInterface):

    config: DictConfig | ListConfig

    def boot(self) -> None:
        self.register_service_providers()

    def register_service_providers(self) -> None:
        providers = self.config.app.service_providers
        for provider_module in providers:
            module = import_module(provider_module)
            provider: ServiceProvider = getattr(
                module, providers[provider_module])

            service_provider = provider(
                app=self,
                config=self.config
            )
            service_provider.boot()

    def boot_service_providers(self) -> None:
        return super().boot_service_providers()

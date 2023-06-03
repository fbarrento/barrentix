from abc import ABC, abstractmethod


class AbstractApplication(ABC):

    @abstractmethod
    def boot(self) -> None:
        return NotImplementedError

    @abstractmethod
    def register_service_providers(self) -> None:
        return NotImplementedError

    @abstractmethod
    def boot_service_providers(self) -> None:
        return NotImplementedError

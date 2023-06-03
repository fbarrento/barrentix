from barrentix.contracts.foundation import AbstractApplication
from barrentix.foundation.application import Application
from barrentix.foundation.config_loader import DictConfig, ListConfig
from barrentix.console.kernel import ConsoleKernel as MainConsoleKernel
from tests.fixtures.config import config  # type: ignore # noqa
from tests.fixtures.foundation.kernel import (  # noqa
    console_kernel,  # type: ignore
    ConsoleKernel
)


class TestApplication:

    def test_application_implements_the_interface(
        self,
        config: DictConfig | ListConfig  # noqa
    ):
        application = Application(config)
        assert isinstance(application, AbstractApplication)

    def test_application_can_add_a_singleton_dependency(
        self,
        config: DictConfig | ListConfig,  # noqa
    ):
        application = Application(config)

        application.singleton(
            name=ConsoleKernel,
            dependency=ConsoleKernel
        )

        kernel = application.make(ConsoleKernel)

        assert isinstance(kernel, MainConsoleKernel)

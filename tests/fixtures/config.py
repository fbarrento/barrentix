from pytest import fixture
from barrentix.foundation.config_loader import (
    ConfigLoader, DictConfig, ListConfig
)


@fixture
def config() -> DictConfig | ListConfig:

    return ConfigLoader().load("tests.files.config")

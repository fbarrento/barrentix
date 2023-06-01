from omegaconf import DictConfig
from barrentix.foundation.config_loader import ConfigLoader


class TestConfigLoader():

    def test_it_can_get_a_modules_path(self):

        loader = ConfigLoader()
        config = loader.load_from_module("tests.files.config")

        assert "version" in config.app

        assert isinstance(config, DictConfig)

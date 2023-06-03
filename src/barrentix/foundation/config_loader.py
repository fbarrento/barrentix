
from typing import List, Dict, Any
from dataclasses import dataclass, field
from omegaconf import OmegaConf, DictConfig, ListConfig
from barrentix.contracts.foundation.loader import AbstractLoader


@dataclass
class ConfigLoader(AbstractLoader):
    config: DictConfig | ListConfig = field(
        default_factory=lambda: OmegaConf.create())

    def _make_dict_from_modules(
            self,
            module: str,
            modules: List[str]
    ) -> Dict[str, Any]:
        config: Dict[str, Any] = {}
        for module_name in modules:
            name = f"{module}.{module_name}"
            try:
                imported_module = self._import_module(name)
                if hasattr(imported_module, "config"):
                    config[module_name] = imported_module.config()
            except AttributeError:
                raise ValueError(
                    f"Please check if the file {name}.py has a config() function."  # noqa
                )

        return config

    def load(self, module: str) -> DictConfig | ListConfig:
        modules = self._make_modules_names(module=module)

        dict_configs = self._make_dict_from_modules(
            module=module,
            modules=modules
        )

        self.config = OmegaConf.merge(self.config, dict_configs)
        return self.config

import glob
import importlib
from typing import List, Dict, Any
from types import ModuleType
from os.path import dirname, basename, isfile, join
from dataclasses import dataclass, field
from omegaconf import OmegaConf, DictConfig, ListConfig
from pathlib import Path


@dataclass
class ConfigLoader():
    config: DictConfig | ListConfig = field(
        default_factory=lambda: OmegaConf.create())

    def _file_paths(self, path: Path) -> List[str]:
        return glob.glob(
            join(Path(path, "*.py"))
        )

    def _make_modules_names(self, path: Path) -> List[str]:
        return [
            basename(f)[:-3] for f in self._file_paths(path=path)
            if isfile(f) and not f.__str__().endswith('__init__.py')
        ]

    def _import_module(self, module: str) -> ModuleType:
        return importlib.import_module(module)

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

    def load_from_module(self, module: str) -> DictConfig | ListConfig:
        imported_module = self._import_module(module)
        modules = self._make_modules_names(
            Path(dirname(imported_module.__file__.__str__()))
        )

        dict_configs = self._make_dict_from_modules(
            module=module,
            modules=modules
        )

        self.config = OmegaConf.merge(self.config, dict_configs)
        return self.config

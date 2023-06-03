import glob
import importlib
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Any
from types import ModuleType
from os.path import dirname, basename, isfile, join


class AbstractLoader(ABC):

    def _file_paths(self, path: Path) -> List[str]:
        return glob.glob(
            join(Path(path, "*.py"))
        )

    def _make_file_paths(self, path: Path) -> List[Path]:
        paths = self._file_paths(path=path)
        return [Path(path) for path in paths]

    def _make_modules_names(self, module: str) -> List[str]:

        imported_module = self._import_module(module)
        path = Path(dirname(imported_module.__file__.__str__()))

        return [
            basename(f)[:-3] for f in self._file_paths(path=path)
            if isfile(f) and not f.__str__().endswith('__init__.py')
        ]

    def _import_module(self, module: str) -> ModuleType:
        return importlib.import_module(module)

    @abstractmethod
    def load(self, module: str) -> Any:
        raise NotImplementedError

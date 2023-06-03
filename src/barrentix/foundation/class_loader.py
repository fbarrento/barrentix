from typing import Any
from .loader import AbstractLoader


class ClassLoader(AbstractLoader):

    def load(self, module: str) -> Any:
        name = module.split(".")[-1]

        # TODO: Move this to a string helper class
        class_name = name.replace("_", " ").title().replace(" ", "")

        imported_module = self._import_module(module=module)
        if hasattr(imported_module, class_name):
            return getattr(imported_module, class_name)

        print(name)

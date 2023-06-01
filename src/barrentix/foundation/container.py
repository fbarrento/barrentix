from inspect import signature
from typing import Dict, Any, Callable
from barrentix.contracts.foundation.container import ContainerInterface


class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


class Container(ContainerInterface, SingletonClass):
    _dependencies: Dict[str | Callable[..., Any], Any] = {}

    def register(
        self,
        name: str | Callable[..., Any],
        dependency: Any
    ) -> None:
        self._dependencies[name] = dependency

    def resolve(self, name: str) -> Any:
        return self._dependencies[name]


def inject(callable: Any) -> Any:
    description = signature(callable)

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        new_attributes = kwargs
        for parameter_name in description.parameters:
            parameter = description.parameters[parameter_name]
            annotation = parameter.annotation

            container = Container()
            new_attributes[parameter_name] = container.resolve(annotation)
            print(annotation)

        value = callable(*args, **kwargs)
        return value

    return wrapper

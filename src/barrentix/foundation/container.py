from inspect import signature
from typing import Dict, Any, Callable, Type
from barrentix.contracts.foundation import AbstractContainer


class Container(AbstractContainer):
    _dependencies: Dict[str | Callable[..., Any], Any] = {}

    def bind(
        self,
        name: str | Callable[..., Any] | Type[Any],
        dependency: Any
    ) -> None:
        self._dependencies[name] = dependency

    def singleton(
        self,
        name: str | Callable[..., Any] | Type[Any],
        dependency: Any
    ) -> None:
        if isinstance(dependency, Callable):
            self._dependencies[name] = dependency()
        else:
            self._dependencies[name] = dependency

    def resolve(
            self,
            name: str | Callable[..., Any] | Type[Any]
    ) -> Any:
        try:
            return self._dependencies[name]
        except Exception:
            return None

    def make(
        self,
        name: str | Callable[..., Any] | type
    ) -> Any:
        return self._dependencies[name]


def inject(callable: Any) -> Any:
    description = signature(callable)

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        new_attributes = kwargs
        for parameter_name in description.parameters:
            parameter = description.parameters[parameter_name]
            annotation = parameter.annotation

            container = Container()
            dependency = container.resolve(annotation)
            if dependency:
                new_attributes[parameter_name] = dependency

        value = callable(*args, **kwargs)
        return value

    return wrapper

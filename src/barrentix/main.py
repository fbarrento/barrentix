import functools
from inspect import signature
from typing import Callable, Any
from contracts.foundation import ApplicationInterface


def inject(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        t = signature(func)
        print(t)
        value = func(*args, **kwargs)

        return value

    return wrapper


@inject
def hello(message: str, app: ApplicationInterface):
    print("From hello function")


say_hello = hello(message="Hello")
print(say_hello)

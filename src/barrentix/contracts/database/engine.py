from typing import Any
from abc import ABCMeta, abstractmethod
from sqlalchemy import URL, Engine


class EngineInterface(metaclass=ABCMeta):

    @abstractmethod
    def make_url(self, config: Any) -> URL:
        raise NotImplementedError

    @abstractmethod
    def create(self, config: Any) -> Engine:
        raise NotImplementedError

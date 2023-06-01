from typing import Any
from sqlalchemy import URL, create_engine, Engine as AlchemyEngine
from barrentix.contracts.database import EngineInterface


class BaseEngine(EngineInterface):

    def make_url(self, config: Any) -> URL:
        return super().make_url(config)

    def create(self, config: Any) -> AlchemyEngine:
        return create_engine(
            self.make_url(config)
        )

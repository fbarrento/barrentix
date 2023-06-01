from typing import Any
from sqlalchemy import URL
from .base_engine import BaseEngine


class SqliteEngine(BaseEngine):

    def make_url(self, config: Any) -> URL:
        return URL.create(
            drivername="sqlite",
            database=config.database
        )

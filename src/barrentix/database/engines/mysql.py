from typing import Any
from sqlalchemy import URL
from .base_engine import BaseEngine


class MySqlEngine(BaseEngine):

    def make_url(self, config: Any) -> URL:
        drivername = config.database.drivername
        if config.database.dbapi:
            drivername = f"{drivername}+{config.database.dbapi}"
        return URL.create(
            drivername=drivername,
            username=config.database.username,
            password=config.database.password,
            host=config.database.host,
            port=config.database.port,
            database=config.database
        )

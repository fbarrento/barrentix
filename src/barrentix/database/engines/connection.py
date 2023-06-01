from sqlalchemy import Connection, Engine as AlchemyEngine
from typing import Dict, Any, Type
from barrentix.contracts.database import EngineInterface
from barrentix.database.engines import (
    MySqlEngine,
    PostgreSqlEngine,
    SqliteEngine
)
# TODO: pip install psycopg2-binary


class Engine():

    def __init__(self, config: Any) -> None:
        engine_class = self.get_driver(config.database.drivername)
        self._engine: AlchemyEngine = engine_class().create(config)

    def connect(self) -> Connection:
        return self._engine.connect()

    def get_driver(self, drivername: str) -> Type[EngineInterface]:
        try:
            return self.drivers[drivername]
        except KeyError:
            raise Exception(
                "Please check the drivername on the database configuration")

    @property
    def drivers(
            self
    ) -> Dict[str, Type[EngineInterface]]:
        return {
            "sqlite": SqliteEngine,
            "postgresql": PostgreSqlEngine,
            "mysql": MySqlEngine
        }

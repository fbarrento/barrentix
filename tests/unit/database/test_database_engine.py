from dataclasses import dataclass, field
from barrentix.database.engines.connection import Engine
from sqlalchemy import text


@dataclass
class PostgreSqlDatabaseConfig:
    drivername: str = "postgresql"
    dbapi: str = "psycopg2"
    username: str = "postgres"
    password: str = "secret"
    host: str = "localhost"
    port: int = 5432
    database: str = "barrentix"


@dataclass
class BaseConfig:
    database: PostgreSqlDatabaseConfig = field(
        default_factory=lambda: PostgreSqlDatabaseConfig()
    )


class TestDatabaseEngine():

    def test_it_connects_to_a_database(self):

        engine = Engine(
            config=BaseConfig()
        )

        conn = engine.connect()
        response = conn.execute(text("SELECT * FROM users"))

        for row in response:
            print(row)

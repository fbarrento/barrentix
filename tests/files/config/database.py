from typing import Dict, Any
from os import environ


def config() -> Dict[str, Any]:
    return {
        "default": {
            "drivername": environ.get("DATABASE_DRIVER", "postgresql"),
            "dbapi": environ.get("DATABASE_DBAPI", "psycopg2"),
            "host":  environ.get("DATABASE_HOST", "localhost"),
            "database": environ.get("DATABASE", "barrentix"),
            "username": environ.get("DATABASE_USERNAME", "barrentix"),
            "password": environ.get("DATABASE_PASSWORD", "secret"),
            "port": environ.get("DATABASE_PORT", 5432),
        }
    }

from typing import Dict, Any
from os import environ, path
from pathlib import Path


def config() -> Dict[str, Any]:
    return {
        "name": environ.get("NAME", "Barrentix"),

        "version": "0.0.1",
        # The application environment.
        "environment": environ.get("ENVIRONMENT", "local"),

        # Whether the application should run or not with the
        # debug activated.
        "debug": environ.get("DEBUG", True),

        "paths": {
            "base": Path(path.dirname(
                path.dirname(
                    path.dirname(__file__)
                )
            )),
            "storage": "${app.paths.base}/storage",
            "tests": "${app.paths.base}",
            "barrentix": "${app.paths.base}/../src/barrentix"
        },

        # Service Providers
        "service_providers": {
            "app.providers.app_service_provider": "AppServiceProvider"
        },
        # "app.providers.database_service_provider",
        # "app.providers.http_service_provider"

    }

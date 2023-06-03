from barrentix.foundation import (
    Application,
    ConfigLoader
)

config = ConfigLoader().load("tests.files.config")


def app() -> Application:
    app = Application(config)
    app.boot()
    return app

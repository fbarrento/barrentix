from pytest import fixture
from barrentix.foundation import ConfigLoader
from barrentix.foundation import Application


@fixture
def app() -> Application:

    app = Application(
        config=ConfigLoader().load("tests.files.config")
    )

    return app

from barrentix.contracts.foundation import ApplicationInterface
from barrentix.foundation.application import Application


class TestApplication:
    def test_application_implements_the_interface(self):
        application = Application()
        assert isinstance(application, ApplicationInterface)

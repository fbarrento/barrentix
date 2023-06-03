from barrentix.foundation import Container
from barrentix.contracts.foundation import AbstractContainer


class DummyClass:
    def __init__(self) -> None:
        self.message = "Hello from Dummy Class"


class TestContainer:
    def test_it_can_create_the_container(self):
        container = Container()

        assert isinstance(container, AbstractContainer)

    def test_it_can_register_a_dependency(self):
        container = Container()
        container.bind(name=type(DummyClass), dependency=DummyClass())

        assert type(DummyClass) in container._dependencies.keys()  # type:ignore # noqa

    def test_it_can_resolve_a_dependency(self):
        container = Container()
        container.bind(name=type(DummyClass), dependency=DummyClass())
        dummy = container.resolve(type(DummyClass))
        assert isinstance(dummy, DummyClass)
        assert dummy.message == "Hello from Dummy Class"

    def test_inject_injects_a_dependency_on_a_function(self):
        container = Container()
        container.bind(name=DummyClass, dependency=DummyClass())
        from barrentix.foundation.container import inject

        @inject
        def i_am_injected(dummy: DummyClass):
            return dummy.message

        injected = i_am_injected()
        assert injected == "Hello from Dummy Class"

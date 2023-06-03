from barrentix.foundation.class_loader import ClassLoader
from tests.fixtures.loader_example import LoaderExample


class TestClassLoader():

    def test_it_can_load_a_class(self):

        loader = ClassLoader().load("tests.fixtures.loader_example")
        loader_instance = loader()

        assert isinstance(loader_instance, LoaderExample)

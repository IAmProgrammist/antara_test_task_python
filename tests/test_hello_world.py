from eventssorter.main import get_hello_world


def test_get_hello_world():
    assert get_hello_world() == "Hello, World!"

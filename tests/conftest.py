import datetime
import pytest
from eventssorter.eventfabric import EventFabric


@pytest.fixture(scope="session")
def event_fabric_params():
    return 100, datetime.datetime(2024, 3, 27), datetime.datetime(2024, 3, 31)


@pytest.fixture(scope="session")
def valid_event_data(event_fabric_params):
    return EventFabric.generate_time(event_fabric_params[1], event_fabric_params[2]), \
        EventFabric.generate_event_type(), \
        EventFabric.generate_participants(), \
        EventFabric.generate_address(), \
        EventFabric.generate_name()


@pytest.fixture(scope="session")
def invalid_event_data():
    return ["Hello World!"], [42], [42, {"Alexander", "Ivan", 42}], \
        [42], [42, "A veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" +
               "eeeeeeeeeeeeeeeeeery long party!"]

import datetime
import pytest
from eventssorter.eventfabric import EventFabric
from eventssorter.event import EventType


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


@pytest.fixture(scope="module")
def valid_events_storage():
    source = {"events": [EventFabric.generate_event(datetime.datetime(2024, 1, 1, hour=0, tzinfo=datetime.timezone.utc),
                                                    datetime.datetime(2024, 1, 1, hour=11,
                                                                      tzinfo=datetime.timezone.utc)).to_dict(),
                         EventFabric.generate_event(
                             datetime.datetime(2024, 1, 1, hour=12, tzinfo=datetime.timezone.utc),
                             datetime.datetime(2024, 1, 1, hour=15,
                                               tzinfo=datetime.timezone.utc)).to_dict(),
                         EventFabric.generate_event(
                             datetime.datetime(2024, 1, 2, hour=12, tzinfo=datetime.timezone.utc),
                             datetime.datetime(2024, 1, 2, hour=15,
                                               tzinfo=datetime.timezone.utc)).to_dict(),
                         EventFabric.generate_event(datetime.datetime(2024, 1, 2, hour=0, tzinfo=datetime.timezone.utc),
                                                    datetime.datetime(2024, 1, 2, hour=11,
                                                                      tzinfo=datetime.timezone.utc)).to_dict(),
                         EventFabric.generate_event(
                             datetime.datetime(2024, 1, 4, hour=12, tzinfo=datetime.timezone.utc),
                             datetime.datetime(2024, 1, 4, hour=15,
                                               tzinfo=datetime.timezone.utc)).to_dict(),
                         EventFabric.generate_event(datetime.datetime(2024, 1, 4, hour=0, tzinfo=datetime.timezone.utc),
                                                    datetime.datetime(2024, 1, 4, hour=5,
                                                                      tzinfo=datetime.timezone.utc)).to_dict(),
                         EventFabric.generate_event(datetime.datetime(2024, 1, 4, hour=6, tzinfo=datetime.timezone.utc),
                                                    datetime.datetime(2024, 1, 4, hour=8,
                                                                      tzinfo=datetime.timezone.utc)).to_dict()
                         ], "grouped_events": {}}

    group_1_jan = list(filter(lambda x: x["type"] != EventType.OTHER, [source["events"][0], source["events"][1]]))
    if group_1_jan:
        source["grouped_events"]["1.1.2024"] = group_1_jan

    group_2_jan = list(filter(lambda x: x["type"] != EventType.OTHER, [source["events"][3], source["events"][2]]))
    if group_2_jan:
        source["grouped_events"]["2.1.2024"] = group_2_jan

    group_4_jan = list(filter(lambda x: x["type"] != EventType.OTHER,
                              [source["events"][5], source["events"][6], source["events"][4]]))
    if group_4_jan:
        source["grouped_events"]["4.1.2024"] = group_4_jan

    return source


@pytest.fixture(scope="session")
def empty_temp_storage_file(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("data.json")
    return fn


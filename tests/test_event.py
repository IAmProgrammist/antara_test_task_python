import datetime
import pytest
from eventssorter.event import Event, EventType


def test_time(valid_event_data, invalid_event_data):
    event = Event()

    current_date = valid_event_data[0]
    event.time = current_date
    assert event.time == current_date

    for invalid_data in invalid_event_data[0]:
        with pytest.raises(ValueError):
            event.time = invalid_data


def test_time_utc(valid_event_data):
    event = Event()

    event.time = valid_event_data[0]
    assert event.time_utc() == datetime.datetime.fromtimestamp(valid_event_data[0].timestamp(), datetime.timezone.utc)


def test_type(valid_event_data, invalid_event_data):
    event = Event()

    current_type = valid_event_data[1]
    event.type = current_type
    assert event.type == current_type

    for invalid_data in invalid_event_data[1]:
        with pytest.raises(ValueError):
            event.type = invalid_data


def test_participants(valid_event_data, invalid_event_data):
    event = Event()

    current_participants = valid_event_data[2]
    event.participants = current_participants
    assert event.participants == current_participants

    for invalid_data in invalid_event_data[2]:
        with pytest.raises(ValueError):
            event.participants = invalid_data


def test_address(valid_event_data, invalid_event_data):
    event = Event()

    current_address = valid_event_data[3]
    event.address = current_address
    assert event.address == current_address

    for invalid_data in invalid_event_data[3]:
        with pytest.raises(ValueError):
            event.address = invalid_data


def test_name(valid_event_data, invalid_event_data):
    event = Event()

    current_name = valid_event_data[4]
    event.name = current_name
    assert event.name == current_name

    for invalid_data in invalid_event_data[4]:
        with pytest.raises(ValueError):
            event.name = invalid_data


def test_to_dict(valid_event_data):
    expected = {
        "time": valid_event_data[0].isoformat(),
        "type": valid_event_data[1].value,
        "name": valid_event_data[4],
        "participants": valid_event_data[2],
        "address": valid_event_data[3]
    }

    actual = Event(time=valid_event_data[0], event_type=valid_event_data[1],
                   name=valid_event_data[4], participants=valid_event_data[2],
                   address=valid_event_data[3]).to_dict()

    assert expected == actual


def test_from_dict(valid_event_data):
    event = Event.from_dict({
        "time": valid_event_data[0].isoformat(),
        "type": valid_event_data[1].value,
        "name": valid_event_data[4],
        "participants": valid_event_data[2],
        "address": valid_event_data[3]
    })

    assert event.time == valid_event_data[0]
    assert event.type == valid_event_data[1]
    assert event.name == valid_event_data[4]
    assert event.participants == valid_event_data[2]
    assert event.address == valid_event_data[3]

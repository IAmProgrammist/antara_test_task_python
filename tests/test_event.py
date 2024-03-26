import datetime

import pytest

import json

from eventssorter.event import Event, EventType


def test_time():
    event = Event()

    current_date = datetime.datetime.fromisoformat('2019-01-04T16:41:24+02:00')
    event.time = current_date
    assert event.time == current_date

    current_date = datetime.datetime.now()
    event.time = current_date
    assert event.time == current_date

    current_date = datetime.datetime.fromisoformat('2019-01-04T16:41:24-02:00')
    event.time = current_date
    assert event.time == current_date

    with pytest.raises(ValueError):
        event.time = "Hello World!"


def test_time_utc():
    event = Event()

    current_date = datetime.datetime.fromisoformat('2019-01-04T16:41:24+02:00')
    event.time = current_date
    assert event.time_utc() == datetime.datetime.fromisoformat('2019-01-04T14:41:24+00:00')

    current_date = datetime.datetime.fromisoformat('2019-01-04T16:41:24-02:00')
    event.time = current_date
    assert event.time_utc() == datetime.datetime.fromisoformat('2019-01-04T18:41:24+00:00')


def test_type():
    event = Event()
    current_type = EventType("private")
    event.type = current_type
    assert event.type == current_type

    with pytest.raises(ValueError):
        event.type = 42


def test_name():
    event = Event()
    current_name = "Party!"
    event.name = current_name
    assert event.name == current_name

    with pytest.raises(ValueError):
        event.name = 42

    with pytest.raises(ValueError):
        event.name = "A veeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeery" \
                     " long party!"


def test_participants():
    event = Event()
    current_participants = ["Alexander", "Ivan", "Robert"]
    event.participants = current_participants
    assert event.participants == current_participants

    with pytest.raises(ValueError):
        event.participants = 42

    with pytest.raises(ValueError):
        event.participants = {"Alexander", "Ivan", 42}


def test_address():
    event = Event()
    current_address = "telegram"
    event.address = current_address
    assert event.address == current_address

    with pytest.raises(ValueError):
        event.address = 42


def test_json_source():
    event = Event(json.loads('{\
  "time": "2019-01-04T16:41:24+02:00",\
  "type": "other",\
  "name": "Party",\
  "participants": ["Alexander", "Ivan", "Robert"],\
  "address": "telegram"\
}'))
    assert event.time == datetime.datetime.fromisoformat('2019-01-04T16:41:24+02:00')
    assert event.type == EventType.OTHER
    assert event.name == "Party"
    assert event.participants == ["Alexander", "Ivan", "Robert"]
    assert event.address == "telegram"

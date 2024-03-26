import datetime

import pytest

from eventssorter.event import Event, EventType


def test_time():
    event = Event()
    current_date = datetime.datetime.now()
    event.time = current_date
    assert event.time == current_date

    with pytest.raises(ValueError):
        event.time = "Hello World!"


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
    current_participants = {"Alexander", "Ivan", "Robert"}
    event.participants = current_participants
    assert event.participants == current_participants

    with pytest.raises(ValueError):
        event.participants = 42

    with pytest.raises(ValueError):
        event.participants = {"Alexander", "Ivan", 42}

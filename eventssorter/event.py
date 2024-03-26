from enum import Enum
import datetime


class EventType(str, Enum):
    PRIVATE = "private"
    MEETING = "meeting"
    CORPORATE = "corporate"
    OTHER = "other"


class Event:
    def __init__(self, json_source=None, time=datetime.datetime.now(datetime.timezone.utc), event_type=EventType.PRIVATE,
                 name="", participants=None, address=""):
        if participants is None:
            participants = {}
        if json_source:
            pass
        else:
            self.__time = time
            self.__type = event_type
            self.__name = name
            self.__participants = participants
            self.__address = address

    @property
    def time(self) -> datetime.datetime:
        return self.__time

    @time.setter
    def time(self, v: datetime.datetime):
        if isinstance(v, datetime.datetime):
            self.__time = v
        else:
            raise ValueError

    @property
    def type(self) -> EventType:
        return self.__type

    @type.setter
    def type(self, v: EventType):
        if isinstance(v, EventType):
            self.__type = v
        else:
            raise ValueError

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, v: str):
        if isinstance(v, str) and len(v) <= 100:
            self.__name = v
        else:
            raise ValueError

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, v):
        if isinstance(v, set) and all(isinstance(participant, str) for participant in v):
            self.__participants = v
        else:
            raise ValueError

from enum import Enum
import datetime
import json


class EventType(str, Enum):
    PRIVATE = "private"
    MEETING = "meeting"
    CORPORATE = "corporate"
    OTHER = "other"


class Event:
    def __init__(self, json_source=None, time=datetime.datetime.now(datetime.timezone.utc), event_type=EventType.PRIVATE,
                 name="", participants=None, address=""):
        if participants is None:
            participants = set()
        if json_source:
            self.time = datetime.datetime.fromisoformat(json_source["time"])
            self.type = json_source["type"]
            self.name = json_source["name"]
            self.participants = json_source["participants"]
            self.address = json_source["address"]
        else:
            self.time = time
            self.type = event_type
            self.name = name
            self.participants = participants
            self.address = address

    def time_utc(self):
        return self.__time_utc

    @property
    def time(self) -> datetime.datetime:
        result = self.__time_utc
        if self.__time_tzinfo:
            result += self.__time_tzinfo.utcoffset(None)

        return result.replace(tzinfo=self.__time_tzinfo)

    @time.setter
    def time(self, v: datetime.datetime):
        if isinstance(v, datetime.datetime):
            self.__time_tzinfo = v.tzinfo
            self.__time_utc = v.replace(tzinfo=datetime.timezone.utc)
            if self.__time_tzinfo:
                self.__time_utc -= self.__time_tzinfo.utcoffset(None)
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

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, v: str):
        if isinstance(v, str):
            self.__address = v
        else:
            raise ValueError

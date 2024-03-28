from enum import Enum
import datetime


class EventType(str, Enum):
    PRIVATE = "private"
    MEETING = "meeting"
    CORPORATE = "corporate"
    OTHER = "other"


class Event:
    MAX_NAME_LEN = 100
    __SCHEME_NAME_TIME = "time"
    __SCHEME_NAME_TYPE = "type"
    __SCHEME_NAME_NAME = "name"
    __SCHEME_NAME_PARTICIPANTS = "participants"
    __SCHEME_NAME_ADDRESS = "address"

    def __init__(self, time=datetime.datetime.now(datetime.timezone.utc),
                 event_type=EventType.PRIVATE,
                 name="", participants=None, address=""):
        if participants is None:
            participants = set()

        self.time = time
        self.type = event_type
        self.name = name
        self.participants = participants
        self.address = address

    def time_utc(self):
        return self.__time_utc

    @property
    def time(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.__time_utc.timestamp(), tz=self.__time_tzinfo)

    @time.setter
    def time(self, v: datetime.datetime):
        if isinstance(v, datetime.datetime):
            self.__time_tzinfo = v.tzinfo
            self.__time_utc = datetime.datetime.fromtimestamp(v.timestamp(), tz=datetime.timezone.utc)
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
        if isinstance(v, str) and len(v) <= Event.MAX_NAME_LEN:
            self.__name = v
        else:
            raise ValueError

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, v):
        if hasattr(v, "__iter__") and all(isinstance(participant, str) for participant in v):
            self.__participants = list(v)
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

    def to_dict(self):
        result = dict()

        result[Event.__SCHEME_NAME_TIME] = self.time.isoformat()
        result[Event.__SCHEME_NAME_TYPE] = self.type.value
        result[Event.__SCHEME_NAME_NAME] = self.name
        result[Event.__SCHEME_NAME_PARTICIPANTS] = self.participants
        result[Event.__SCHEME_NAME_ADDRESS] = self.address

        return result

    @classmethod
    def from_dict(cls, source):
        return cls(time=datetime.datetime.fromisoformat(source[Event.__SCHEME_NAME_TIME]),
                   event_type=EventType(source[Event.__SCHEME_NAME_TYPE]),
                   name=source[Event.__SCHEME_NAME_NAME],
                   participants=source[Event.__SCHEME_NAME_PARTICIPANTS],
                   address=source[Event.__SCHEME_NAME_ADDRESS])

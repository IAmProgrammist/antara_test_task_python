from enum import Enum
import datetime
import random


class EventType(str, Enum):
    PRIVATE = "private"
    MEETING = "meeting"
    CORPORATE = "corporate"
    OTHER = "other"


class Event:
    max_name_len = 100

    def __init__(self, json_source=None, time=datetime.datetime.now(datetime.timezone.utc),
                 event_type=EventType.PRIVATE,
                 name="", participants=None, address=""):
        if participants is None:
            participants = set()
        if json_source:
            self.time = datetime.datetime.fromisoformat(json_source["time"])
            self.type = EventType(json_source["type"])
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
        if isinstance(v, str) and len(v) <= Event.max_name_len:
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


class EventFabric:
    participants = ["Mary Williams", "Timothy Smith", "Debra Thompson", "Brandy Murray", "Hazel Edwards",
                    "Laura Allen", "Larry Townsend", "Mary Snyder", "Lawrence Jones", "Teresa Williamson"]
    max_word_len = 20
    @staticmethod
    def generate_events(amount=1, begin_date=datetime.datetime(2024, 1, 1), end_date=datetime.datetime(2030, 1, 1)):
        return [EventFabric.generate_event(begin_date, end_date) for _ in range(0, amount)]

    @staticmethod
    def generate_event(begin_date=datetime.datetime(2024, 1, 1), end_date=datetime.datetime(2030, 1, 1)):
        if end_date < begin_date:
            raise ValueError

        time_delta = (end_date - begin_date) * random.random()
        time = begin_date + time_delta
        random_offset = int(24 * random.random()) * 60
        random_offset = random_offset - (random_offset % 30) - 12 * 60
        time -= datetime.timedelta(minutes=random_offset)
        time = time.replace(tzinfo=datetime.timezone(datetime.timedelta(minutes=random_offset)))

        event_type = random.choice(list(EventType))

        name = ""
        name_len = random.randint(1, Event.max_name_len)
        word_len = random.randint(1, EventFabric.max_word_len)
        while len(name) < name_len:
            if word_len > 0:
                name += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                word_len -= 1
            else:
                name += " "
                word_len = random.randint(1, EventFabric.max_word_len)

        participants = random.choices(EventFabric.participants, k=random.randint(2, len(EventFabric.participants)))

        address = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k=20))

        return Event(time=time, event_type=event_type, participants=participants, address=address, name=name)
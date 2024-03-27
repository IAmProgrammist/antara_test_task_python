import datetime
import random

from eventssorter.event import EventType, Event


class EventFabric:
    __PARTICIPANTS = ["Mary Williams", "Timothy Smith", "Debra Thompson", "Brandy Murray", "Hazel Edwards",
                      "Laura Allen", "Larry Townsend", "Mary Snyder", "Lawrence Jones", "Teresa Williamson"]
    __MAX_WORD_LEN = 20

    @staticmethod
    def generate_time(begin_date=datetime.datetime(2024, 1, 1), end_date=datetime.datetime(2030, 1, 1)):
        if end_date < begin_date:
            raise ValueError

        time_delta = (end_date - begin_date) * random.random()
        time = begin_date + time_delta
        random_offset = int(24 * random.random() * 2) * 30 - 12 * 60
        time += datetime.timedelta(minutes=random_offset)
        return time.replace(tzinfo=datetime.timezone(datetime.timedelta(minutes=random_offset)))

    @staticmethod
    def generate_event_type():
        return random.choice(list(EventType))

    @staticmethod
    def generate_name():
        name = ""
        name_len = random.randint(1, Event.MAX_NAME_LEN)
        word_len = random.randint(1, EventFabric.__MAX_WORD_LEN)
        while len(name) < name_len:
            if word_len > 0:
                name += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                word_len -= 1
            else:
                name += " "
                word_len = random.randint(1, EventFabric.__MAX_WORD_LEN)

        return name

    @staticmethod
    def generate_participants():
        return random.choices(EventFabric.__PARTICIPANTS, k=random.randint(2, len(EventFabric.__PARTICIPANTS)))

    @staticmethod
    def generate_address():
        return "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k=20))

    @staticmethod
    def generate_events(amount=1, begin_date=datetime.datetime(2024, 1, 1), end_date=datetime.datetime(2030, 1, 1)):
        return [EventFabric.generate_event(begin_date, end_date) for _ in range(0, amount)]

    @staticmethod
    def generate_event(begin_date=datetime.datetime(2024, 1, 1), end_date=datetime.datetime(2030, 1, 1)):
        return Event(time=EventFabric.generate_time(begin_date, end_date),
                     event_type=EventFabric.generate_event_type(),
                     participants=EventFabric.generate_participants(),
                     address=EventFabric.generate_address(),
                     name=EventFabric.generate_name())

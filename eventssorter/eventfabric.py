from event import Event, EventType
import datetime
import random


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

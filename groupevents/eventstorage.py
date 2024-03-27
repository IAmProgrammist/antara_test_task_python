import datetime
import json
from groupevents.event import EventType, Event


class EventStorage:
    __SCHEME_NAME_EVENT = "events"
    __SCHEME_NAME_EVENT_GROUPED = "grouped_events"

    def __init__(self, source_dict=None):
        if source_dict is None:
            source_dict = {EventStorage.__SCHEME_NAME_EVENT: []}

        self.events = [Event.from_dict(event) for event in source_dict[EventStorage.__SCHEME_NAME_EVENT]]

    @classmethod
    def load_from_file(cls, path):
        with open(path, 'r') as f:
            return cls(json.load(f))

    @classmethod
    def load_from_dict(cls, data):
        return cls(data)

    @property
    def events(self):
        return self.__events

    @events.setter
    def events(self, v):
        if hasattr(v, "__iter__") and all(isinstance(event, Event) for event in v):
            self.__events = list(v)
        else:
            raise ValueError

    def dump_grouped_by_date_to_dict(self):
        result = dict()
        for event in self.events:
            if event.type == EventType.OTHER:
                continue

            key = f"{event.time_utc().day}.{event.time_utc().month}.{event.time_utc().year}"
            result.setdefault(key, [])
            result[key].append(event)

        for event_key in result.keys():
            result[event_key].sort(key=lambda x: x.time_utc())
            result[event_key] = list(map(lambda x: x.to_dict(), result[event_key]))

        return {EventStorage.__SCHEME_NAME_EVENT_GROUPED: result}

    def dump_grouped_by_date_to_file(self, path):
        with open(path, 'w') as f:
            json.dump(self.dump_grouped_by_date_to_dict(), f)

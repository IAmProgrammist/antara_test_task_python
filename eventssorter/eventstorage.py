import datetime
import json
from eventssorter.event import EventType, Event


class EventStorage:
    __SCHEME_NAME_EVENT = "events"
    __SCHEME_NAME_EVENT_GROUPED = "grouped_events"

    def __init__(self, source=None):
        if source is None:
            source = {EventStorage.__SCHEME_NAME_EVENT: []}

        self.events = [Event.from_dict(event) for event in source[EventStorage.__SCHEME_NAME_EVENT]]

    @classmethod
    def load_from_json(cls, data):
        return cls(json.loads(data))

    @classmethod
    def load_from_file(cls, path):
        with open(path, 'r') as f:
            return cls(json.load(f))

    @classmethod
    def load_from_dict(cls, data):
        return cls(data)

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

    def dump_grouped_by_date_to_json(self):
        return json.dumps(self.dump_grouped_by_date_to_dict())

    def dump_grouped_by_date_to_file(self, path):
        with open(path, 'w') as f:
            json.dump(self.dump_grouped_by_date_to_dict(), f)

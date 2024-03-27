import json
from eventfabric import EventFabric
from eventstorage import EventStorage
import datetime

if __name__ == "__main__":
    events = EventStorage.load_from_dict({"events": [item.to_dict() for item in EventFabric.generate_events(100,
        begin_date=datetime.datetime(2024, 1, 1), end_date=datetime.datetime(2024, 1, 3))]}).to_dict_grouped_by_date()

    events = events

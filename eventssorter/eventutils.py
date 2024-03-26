import json
from event import Event


class EventUtils:
    @staticmethod
    def read_from_file(path: str) -> list:
        with open(path, 'r') as f:
            result = [Event(json_source=source) for source in json.load(f)["events"]]

        return result

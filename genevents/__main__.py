import argparse
import datetime
import json

from groupevents.eventfabric import EventFabric

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Params for storage generation')
    parser.add_argument('output', type=str, help='Output dir for events storage', default="output.json")
    parser.add_argument('amount', type=int, help='Amount of events', default=100)
    parser.add_argument('begindate', type=str, help='Earliest date in events (ISO)',
                        default="2024-01-01T10:00:00.000000-00:00")
    parser.add_argument('enddate', type=str, help='Latest date in events (ISO)',
                        default="2024-01-10T10:00:00.000000-00:00")
    args = parser.parse_args()

    events = {"events": list(map(lambda x: x.to_dict(),
                                 EventFabric.generate_events(args.amount,
                                                             datetime.datetime.fromisoformat(
                                                                 args.begindate),
                                                             datetime.datetime.fromisoformat(
                                                                 args.enddate))))}
    with open(args.output, "w") as f:
        json.dump(events, f)
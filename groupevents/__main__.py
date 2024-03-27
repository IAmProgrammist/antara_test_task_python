import argparse

from groupevents.eventstorage import EventStorage

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Storage to process')
    parser.add_argument('input', type=str, help='Input dir for events storage', default="input.json")
    parser.add_argument('output', type=str, help='Output dir for grouped events storage', default="output.json")
    args = parser.parse_args()

    EventStorage.load_from_file(args.input).dump_grouped_by_date_to_file(args.output)

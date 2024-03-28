import json

import pytest
from groupevents.eventstorage import EventStorage


@pytest.mark.eventstorage_test_load_dump_dict
def test_load_dump_dict(valid_events_storage):
    assert valid_events_storage["grouped_events"] == \
           EventStorage.load_from_dict(valid_events_storage).dump_grouped_by_date_to_dict()["grouped_events"]


@pytest.mark.eventstorage_test_load_dump_file
def test_load_dump_file(valid_events_storage, empty_temp_storage_file):
    EventStorage.load_from_dict(valid_events_storage).dump_grouped_by_date_to_file(empty_temp_storage_file)

    with open(empty_temp_storage_file, 'r') as f:
        assert valid_events_storage["grouped_events"] == json.load(f)["grouped_events"]

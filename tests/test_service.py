"""Service tests.

Test to add:
- Read Employee Profile
"""

import pytest


def test_simple_flow(testapp, identity_simple, example_record):
    """Create a record."""
    # Create an item
    # item = service.create(identity_simple, input_data)
    # id_ = item.id
    with testapp.app_context():
        service = testapp.extensions["invenio-profiles"].service
        # Read it
        read_item = service.read(identity_simple, example_record.id)
        print(read_item.to_dict())
        # assert item.id == read_item.id
        # assert item.data == read_item.data

"""User Employee Profile resource tests."""

import pytest

#
# Read
#
def test_read_self_serialization(client, headers, user_pub):
    """Read self user."""
    client = user_pub.login(client)
    r = client.get(f"/users/{user_pub.id}", headers=headers)
    assert r.status_code == 200

# def test_simple_flow(example_record, client_with_login, headers):
#     """Test a simple REST API flow."""
#     client = client_with_login
#     # Create a draft
#     read_profile_response = client.get(
#         f"/employeeprofile/{example_record.id}",x
#         headers=headers,
#     )
#     assert read_profile_response.status_code == 200
#     print(read_profile_response.json)
#     print(read_profile_response.json.keys())
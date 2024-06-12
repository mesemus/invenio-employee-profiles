import json

from invenio_employee_profiles.proxies import current_profiles_service
from invenio_access.permissions import system_identity

from invenio_employee_profiles.records.api import EmployeeProfile


def test_service_layer(app, db, users, search_clear, search, employee_profile_data):
    u, data = employee_profile_data
    employee_profile = current_profiles_service.create(system_identity, {**data, 'active': True, 'user': {"id": str(u.id)}})

    assert "id" in employee_profile.data
    assert employee_profile.data.items() >= {
      "revision_id": 2,
      "email_address": "johndoe@example.com",
      "biography": "John Doe is a software engineer with over 10 years of experience in the tech industry. He specializes in backend development, particularly with Python and Django. He has a passion for clean, efficient code and enjoys working on complex, challenging problems.",
      "profile_image": "https://example.com/johndoe.png",
      "active": True,
      "user": {
        "id": "1",
        "links": {},
        "is_current_user": False,
        "identities": {},
        "username": "pubres",
        "profile": {
          "full_name": "Tim Smith",
          "affiliations": "CERN"
        }
      }
    }.items()

    EmployeeProfile.index.refresh()

    # try to search for the profile
    all_profiles = current_profiles_service.search(system_identity)
    assert all_profiles.total == 1
    hits = list(all_profiles.hits)
    assert hits[0] == employee_profile.data

    # try to search the profile with user id
    user_profiles = current_profiles_service.search(system_identity, q=f"user.id:{u.id}")
    assert user_profiles.total == 1

    # try to search the profile with different user id
    user_profiles = current_profiles_service.search(system_identity, q=f"user.id:{u.id+10001}")
    assert user_profiles.total == 0
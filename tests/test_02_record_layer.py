from invenio_employee_profiles.records.api import EmployeeProfile


def test_record_create(app, db, users, search_clear, employee_profile_data):
    u, data = employee_profile_data
    profile = EmployeeProfile.create(data, user_id=u.id, active=True)
    assert profile.id is not None

    db.session.expunge_all()

    profile_2 = EmployeeProfile.get_record(profile.id)
    assert profile_2.user_id == u.id
    for k, v in data.items():
        assert profile_2[k] == v
    assert profile_2.active == True

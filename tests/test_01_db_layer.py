from invenio_employee_profiles.records.models import EmployeeProfileModel


def test_db_create(app, db, users, employee_profile_data, search_clear):
    u, data = employee_profile_data
    profile = EmployeeProfileModel(json=data, user_id=u.id, active=True)
    db.session.add(profile)
    db.session.commit()
    profile_id = profile.id

    db.session.expunge_all()

    assert profile_id is not None
    profile_2 = EmployeeProfileModel.query.get(profile_id)

    assert profile_2.user_id == u.id
    assert profile_2.json == data
    assert profile_2.active == True

def test_resource(app, db, users, search_clear, search, employee_profile_data, authenticated_client):
    u, data = employee_profile_data

    with authenticated_client.post('/employee-profiles', json={
        **data,
        'active': True,
        'user': {
            'id': str(u.id),
        }
    }) as response:
        assert response.status_code == 201
        assert response.json.items() >= {
            "email_address": "johndoe@example.com",
            "biography": "John Doe is a software engineer with over 10 years of experience in the tech industry. He specializes in backend development, particularly with Python and Django. He has a passion for clean, efficient code and enjoys working on complex, challenging problems.",
            "profile_image": "https://example.com/johndoe.png",
            "active": True,
            "user": {'id': '1',
              'identities': {},
              'is_current_user': True,
              'links': {},
              'profile': {'affiliations': 'CERN', 'full_name': 'Tim Smith'},
              'username': 'pubres'
            }
        }.items()

# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Test Invenio Records."""

import json
import os
import uuid

import pytest
from flask import Flask
from invenio_accounts.models import Role, User
from invenio_profiles import EmployeeProfileExtension
from invenio_profiles.models import EmployeeProfile


def test_version():
    """Test version import."""
    from invenio_profiles import EmployeeProfileExtension, __version__

    assert EmployeeProfileExtension
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = EmployeeProfileExtension(app)
    assert "invenio-profiles" in app.extensions

    app = Flask("testapp")
    ext = EmployeeProfileExtension()
    assert "invenio-profiles" not in app.extensions
    ext.init_app(app)
    assert "invenio-profiles" in app.extensions


def test_db(testapp, db):
    """Test database backend."""
    with testapp.app_context():
        alice = User(email="alice@inveniosoftware.org")
        admin_role = Role(name="admin")
        admin_role.users.append(alice)
        db.session.add(alice)
        db.session.commit()
        # Create Employee Profile
        alice_profile = EmployeeProfile(
            user=alice,
            email_address="alice@gmail.com",
            biography="fsjkbvjksbvjksdbvjksdv",
        )
        db.session.add(alice_profile)
        db.session.commit()
        assert len(User.query.all()) == 1
        assert len(EmployeeProfile.query.all()) == 1
        assert EmployeeProfile.query.get(1).email_address == "alice@gmail.com"
        assert EmployeeProfile.query.get(1).user.email == "alice@inveniosoftware.org"
    # with pytest.raises(ValueError):
    #     # the profile doesn't expect an 'email' value
    #     user.user_profile = {
    #         **profile,
    #         "email": "admin@inveniosoftware.org",
    #     }

    # assert user.user_profile == {}

    # # a valid profile should be accepted
    # user.user_profile = profile
    # assert dict(user.user_profile) == profile

    # # setting expected properties should work
    # assert len(user.user_profile) == 1
    # assert user.user_profile["full_name"] == "Invenio Admin"

    # # but setting unexpected properties should not work
    # with pytest.raises(ValueError):
    #     user.user_profile["invalid"] = "value"

    # # similar with wrong types for expected fields
    # with pytest.raises(ValueError):
    #     user.user_profile["email"] = 1

    # assert len(user.user_profile) == 1
    # assert user.user_profile["full_name"] == "Invenio Admin"
    # assert (
    #     app.config["ACCOUNTS_DEFAULT_EMAIL_VISIBILITY"]
    #     == user.preferences["email_visibility"]
    # )
    # assert (
    #     app.config["ACCOUNTS_DEFAULT_USER_VISIBILITY"] == user.preferences["visibility"]
    # )

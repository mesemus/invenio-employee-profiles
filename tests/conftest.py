# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


"""Pytest configuration."""

from invenio_app.factory import create_api
import pytest
from flask_principal import Identity, Need, UserNeed
from invenio_cache.proxies import current_cache
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.schema import DropConstraint, DropSequence, DropTable

from marshmallow import fields
from invenio_users_resources.services.schemas import (
    NotificationPreferences,
    UserPreferencesSchema,
)
from invenio_users_resources.proxies import current_users_service
from flask_security import login_user
from invenio_accounts.testutils import login_user_via_session


pytest_plugins = ("celery.contrib.pytest",)


@compiles(DropTable, "postgresql")
def _compile_drop_table(element, compiler, **kwargs):
    return compiler.visit_drop_table(element) + " CASCADE"


@compiles(DropConstraint, "postgresql")
def _compile_drop_constraint(element, compiler, **kwargs):
    return compiler.visit_drop_constraint(element) + " CASCADE"


@compiles(DropSequence, "postgresql")
def _compile_drop_sequence(element, compiler, **kwargs):
    return compiler.visit_drop_sequence(element) + " CASCADE"

@pytest.fixture(scope="module")
def create_app(instance_path, entry_points):
    """Application factory fixture."""
    return create_api


#
# Application
#
@pytest.fixture(scope="module")
def app_config(app_config):
    """Override pytest-invenio app_config fixture."""
    app_config["RECORDS_REFRESOLVER_CLS"] = (
        "invenio_records.resolver.InvenioRefResolver"
    )
    app_config["RECORDS_REFRESOLVER_STORE"] = (
        "invenio_jsonschemas.proxies.current_refresolver_store"
    )
    # Variable not used. We set it to silent warnings
    app_config["JSONSCHEMAS_HOST"] = "not-used"
    # setting preferences schema to test notifications
    app_config["ACCOUNTS_USER_PREFERENCES_SCHEMA"] = UserPreferencesNotificationsSchema

    app_config["USERS_RESOURCES_GROUPS_ENABLED"] = True

    return app_config


@pytest.fixture(scope="module")
def testapp(base_app, database):
    """Application with just a database.

    Pytest-Invenio also initialises ES with the app fixture.
    """
    yield base_app


@pytest.fixture(scope="module")
def identity_simple():
    """Simple identity fixture."""
    i = Identity(1)
    i.provides.add(UserNeed(1))
    i.provides.add(Need(method="system_role", value="any_user"))
    return i


class UserPreferencesNotificationsSchema(UserPreferencesSchema):
    """Schema extending preferences with notification preferences."""

    notifications = fields.Nested(NotificationPreferences)

@pytest.fixture(scope="function", autouse=True)
def clear_cache(app):
    current_cache.cache.clear()


@pytest.fixture(scope="module")
def users_data():
    """Data for users."""
    return [
        {
            "username": "pubres",
            "email": "pubres@inveniosoftware.org",
            "profile": {
                "full_name": "Tim Smith",
                "affiliations": "CERN",
            },
            "preferences": {
                "visibility": "public",
                "email_visibility": "restricted",
            },
        },
    ]


@pytest.fixture()
def users(UserFixture, app, db, users_data):
    """Test users."""
    users = []
    for obj in users_data:
        u = UserFixture(
            username=obj["username"],
            email=obj["email"],
            password=obj["username"],
            user_profile=obj.get("profile"),
            preferences=obj.get("preferences"),
            active=obj.get("active", True),
            confirmed=obj.get("confirmed", True),
        )
        u.create(app, db)
        users.append(u)
    current_users_service.indexer.process_bulk_queue()
    current_users_service.record_cls.index.refresh()
    db.session.commit()
    return users


@pytest.fixture()
def authenticated_client(client, users):
    """Log in a user to the client."""
    user = users[0].user
    login_user(user)
    login_user_via_session(client, email=user.email)
    return client


@pytest.fixture()
def employee_profile_data(users):
    """Data for employee profiles."""
    u = users[0]
    return u.user, {
            "email_address": "johndoe@example.com",
            'biography': "John Doe is a software engineer with over 10 years "
                         "of experience in the tech industry. He specializes in backend development, "
                         "particularly with Python and Django. He has a passion for clean, efficient code "
                         "and enjoys working on complex, challenging problems.",
            'profile_image': 'https://example.com/johndoe.png',
        }


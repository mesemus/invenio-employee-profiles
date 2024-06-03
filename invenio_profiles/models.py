# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2020 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Employee Profile models."""
from invenio_accounts.models import User
from invenio_db import db
from sqlalchemy_utils import Timestamp


class EmployeeProfile(db.Model, Timestamp):
    """User data model."""

    __tablename__ = "profiles_employee"

    id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String, nullable=False)
    biography = db.Column(db.Text, nullable=False)
    profile_image = db.Column(db.String, nullable=True)

    active = db.Column(db.Boolean(name="active"))
    """Flag to say if the user is active or not ."""

    # Enables SQLAlchemy version counter
    version_id = db.Column(db.Integer, nullable=False)
    """Used by SQLAlchemy for optimistic concurrency control."""

    id_user = db.Column(db.Integer(), db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User, backref="employee_profiles")

    __mapper_args__ = {"version_id_col": version_id}

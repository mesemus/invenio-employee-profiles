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

import uuid

from invenio_accounts.models import User
from invenio_db import db
from invenio_records.models import RecordMetadataBase
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils.types import UUIDType


class EmployeeProfileModel(db.Model, RecordMetadataBase):
    __tablename__ = "employee_profiles"

    id = db.Column(UUIDType, primary_key=True, default=uuid.uuid4)

    @declared_attr
    def user_id(cls):
        """Foreign key to the related user."""
        return db.Column(
            db.Integer(),
            db.ForeignKey(User.id, ondelete="RESTRICT"),
            # must be nullable because record service at first creates/commits an empty record and then fills it in
            nullable=True,
        )
    user = db.relationship(User, backref="employee_profiles")

    # added to the "data" part of the profile
    # email_address = db.Column(db.String, nullable=False)
    # biography = db.Column(db.Text, nullable=False)
    # profile_image = db.Column(db.String, nullable=True)

    # kept here for easy searching
    active = db.Column(db.Boolean(name="active"))
    """Flag to say if the user is active or not ."""

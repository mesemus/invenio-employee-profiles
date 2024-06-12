# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2024 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

r"""Invenio-Records is a metadata storage module.

In a few words, a `record`_ is basically a structured collection of fields and
values (metadata) which provides information about other data.

.. _record: https://en.wikipedia.org/wiki/Record_(computer_science)

A record (and each revision) is identified by a unique `UUID`_, as most of the
others entities in Invenio.

.. _UUID: https://en.wikipedia.org/wiki/Universally_unique_identifier

Invenio-Profiles is a core component of Invenio and it provides a way to create,
update and delete records. Records are versioned, to keep track of
modifications and to be able to revert back to a specific revision.

When creating or updating a record, if the record contains a schema definition,
the record data will be validated against its schema. Moreover, data format can
for each field be also validated.

When deleting a record, two options are available:

* **soft deletion**: record will be deletes but keeping its identifier and
  history, to ensure that the same record's identifier cannot be reused, and
  that older revisions can be retrieved.
* **hard deletion**: record will be completely deleted with its history.

Records creation and update can be validated if the schema is provided.

Further documentation available Documentation:
https://invenio-records.readthedocs.io/

Initialization
--------------

Create a Flask application:

>>> import os
>>> db_url = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite://')
>>> from flask import Flask
>>> app = Flask('myapp')
>>> app.config.update({
...     'SQLALCHEMY_DATABASE_URI': db_url,
...     'SQLALCHEMY_TRACK_MODIFICATIONS': False,
... })

Initialize Invenio-Profiles dependencies and Invenio-Records itself:

>>> from invenio_db import InvenioDB
>>> ext_db = InvenioDB(app)

The following examples needs to run in a Flask application context, so
let's push one:

>>> app.app_context().push()

Also, for the examples to work we need to create the database and tables (note,
in this example we use an in-memory SQLite database by default):

>>> from invenio_db import db
>>> db.create_all()

"""
# from .ext import EmployeeProfileExtension

__version__ = "0.0.1"

__all__ = (
#    "EmployeeProfileExtension",
    "__version__",
)

# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology
# Copyright (C) 2022 TU Wien.
# Copyright (C) 2022 European Union.
# Copyright (C) 2022 CERN.
#
# Invenio-Users-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""User Employee Profile Services."""

from invenio_records_resources.services import Service


class EmployeeProfileService(Service):
    """Employee Profile Service class."""

    # This is taken from invenio_records_resources.services.records.service
    # and slightly altered
    def read(self, identity, id_, expand=False, action="read"):
        """Retrieve a record."""
        # Resolve and require permission
        record = self.config.record_cls.query.get(id_)
        self.require_permission(identity, action, record=record)

        # Run components
        for component in self.components:
            if hasattr(component, "read"):
                component.read(identity, record=record)

        return self.config.result_item_cls(identity, record)

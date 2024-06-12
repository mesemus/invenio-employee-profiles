# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 TU Wien.
# Copyright (C) 2022 CERN.
#
# Invenio-Users-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
"""Employee Profile service configuration."""

from invenio_records_resources.services.records import RecordServiceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin

from .permissions import EmployeeProfilePermissionPolicy
from .schema import EmployeeProfileSchema
from ..records.api import EmployeeProfile

from invenio_records_resources.services.records.components import DataComponent, RelationsComponent
from .components import EmployeeProfileServiceComponent


class EmployeeProfileServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    """Employee Profile Service configuration Class."""

    service_id = "employee_profiles"
    record_cls = EmployeeProfile
    schema = EmployeeProfileSchema
    permission_policy_cls = EmployeeProfilePermissionPolicy
    indexer_queue_name = "employee_profiles"

    components = [
        DataComponent,
        RelationsComponent,
        EmployeeProfileServiceComponent,
    ]

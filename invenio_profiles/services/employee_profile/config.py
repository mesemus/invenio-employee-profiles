# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 TU Wien.
# Copyright (C) 2022 CERN.
#
# Invenio-Users-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
"""Employee Profile service configuration."""

from invenio_records_resources.services import ServiceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin

from ...models import EmployeeProfile
from .permissions import EmployeeProfilePermissionPolicy
from .results import RecordView


class EmployeeProfileServiceConfig(ServiceConfig, ConfiguratorMixin):
    """Employee Profile Service configuration Class."""

    service_id = "employee_profiles"
    record_cls = EmployeeProfile
    permission_policy_cls = EmployeeProfilePermissionPolicy
    result_item_cls = RecordView
    # result_list_cls = RecordList
    indexer_queue_name = "employee_profiles"

    # Service components are not mandatory to use, but they help keep service
    # methods clean and readable by separating independent concerns.
    components = [
        # MetadataComponent,
    ]

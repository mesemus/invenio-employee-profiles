"""Config for Employee Profile Resource."""

from invenio_records_resources.resources.records import RecordResourceConfig
from invenio_records_resources.services.base.config import ConfiguratorMixin


class EmployeeProfileResourceConfig(RecordResourceConfig, ConfiguratorMixin):
    """Blueprint configuration."""

    blueprint_name = "employee-profiles"
    url_prefix = "/employee-profiles"

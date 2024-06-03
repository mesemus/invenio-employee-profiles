"""Config for Employee Profile Resource."""

import marshmallow as ma
from flask_resources import (
    create_error_handler,
    HTTPJSONException,
    JSONSerializer,
    ResourceConfig,
    ResponseHandler,
)
from invenio_records_resources.services.base.config import ConfiguratorMixin
from ...services.employee_profile.errors import EmployeeProfileDoesNotExistError


class EmployeeProfileResourceConfig(ResourceConfig, ConfiguratorMixin):
    """Blueprint configuration."""

    blueprint_name = "employeeprofiles"
    url_prefix = "/employeeprofiles"
    routes = {
        "list": "",
        "item": "/<id>",
    }
    # Request parsing
    request_read_args = {"id": ma.fields.Int()}
    response_handlers = {
        # Define JSON serializer for "application/json"
        "application/json": ResponseHandler(JSONSerializer())
    }
    # Set the error handlers to map service errors to HTTP errors.
    error_handlers = {
        EmployeeProfileDoesNotExistError: create_error_handler(
            HTTPJSONException(
                code=404,
                description="Profile doesn't exist.",
            )
        )
    }

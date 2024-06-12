"""Extension for Employee Profile."""
from functools import cached_property

from .resources import EmployeeProfileResourceConfig, EmployeeProfileResource
from .services import EmployeeProfileService, EmployeeProfileServiceConfig


class EmployeeProfileExtension:
    """Employee Profile Extension Class."""

    def __init__(self, app=None):
        """Extension initialization."""
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Extension Initials when app is not None."""

        # in case the app is not passed in the constructor
        self.app = app

        self.init_config(app)
        app.extensions["invenio-employee-profiles"] = self

    @cached_property
    def service(self):
        """Extension initialization of Service."""
        return EmployeeProfileService(config=self._service_config)

    @cached_property
    def resource(self):
        return EmployeeProfileResource(config=self._resource_config, service=self.service)

    # region Private Methods

    @cached_property
    def _service_config(self):
        """Extension initialization of Service configs."""
        return EmployeeProfileServiceConfig.build(self.app)

    @cached_property
    def _resource_config(self):
        """Extension initialization of Resource configs."""
        return EmployeeProfileResourceConfig.build(self.app)

    def init_config(self, app):
        """Setup Extension congig."""
        # ....
        pass

    # endregion

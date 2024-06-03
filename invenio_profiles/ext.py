"""Extension for Employee Profile."""

from .services import EmployeeProfileService, EmployeeProfileServiceConfig
from .resources import EmployeeProfileResource, EmployeeProfileResourceConfig


class EmployeeProfileExtension:
    """Employee Profile Extension Class."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Extension Initials when app is not None."""
        self.init_config(app)
        self.init_services(app)
        self.init_resources(app)
        app.extensions["invenio-profiles"] = self

    def init_config(self, app):
        """Setup Extension congig."""
        # ....
        pass

    def init_services(self, app):
        """Extension initialization of Services."""
        # Prepare all service configs
        configs = self.service_configs(app)
        # Set the services
        self.service = EmployeeProfileService(configs.employee_profile_service)

    def service_configs(self, app):
        """Extension initialization of Service configs."""

        class Configs:
            """Configurations."""

            employee_profile_service = EmployeeProfileServiceConfig.build(app)
            # other service configs could be defined here

        return Configs

    def init_resources(self, app):
        """Initialize resources."""
        self.employee_profiles_resource = EmployeeProfileResource(
            service=self.service,
            config=EmployeeProfileResourceConfig.build(app),
        )
        app.register_blueprint(self.employee_profiles_resource.as_blueprint())

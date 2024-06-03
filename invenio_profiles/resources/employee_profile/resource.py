"""Resource for Employee Profile."""
from flask import g
from flask_resources import (
    Resource,
    route,
    from_conf,
    request_parser,
    resource_requestctx,
    response_handler,
)

#
# Decorators
#
request_read_args = request_parser(from_conf("request_read_args"), location="args")


#
# Resource
#
class EmployeeProfileResource(Resource):
    """Employee Profile Resource class."""

    def __init__(self, config, service):
        """Initialization of resource."""
        super().__init__(config)
        self.service = service
    
    def create_url_rules(self):
        # Get the named routes from the config
        routes = self.config.routes
        # Define the URL rules:
        return [
            route("GET", routes["item"], self.read),
        ]

    @request_read_args
    @response_handler()
    def read(self):
        """Read an item."""
        item = self.service.read(
            g.identity,
            resource_requestctx.view_args["id"],
        )
        return item.to_dict(), 200

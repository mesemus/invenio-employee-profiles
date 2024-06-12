"""Proxies for Profile extension and services."""

from flask import current_app
from werkzeug.local import LocalProxy

current_profiles = LocalProxy(lambda: current_app.extensions["invenio-employee-profiles"])

current_profiles_service = LocalProxy(lambda: current_profiles.service)

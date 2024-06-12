"""Permissions for Employeee Profile service functions."""

from invenio_records_permissions import RecordPermissionPolicy
from invenio_records_permissions.generators import AnyUser, SystemProcess, AuthenticatedUser


class EmployeeProfilePermissionPolicy(RecordPermissionPolicy):
    """Employee Profile Permission Policy class."""

    can_create = [SystemProcess(), AuthenticatedUser()]
    can_read = [AnyUser(), SystemProcess()]
    can_search = [AnyUser(), SystemProcess()]

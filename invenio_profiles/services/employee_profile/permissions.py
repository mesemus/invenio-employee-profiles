"""Permissions for Employeee Profile service functions."""

from invenio_records_permissions import RecordPermissionPolicy
from invenio_records_permissions.generators import AnyUser, SystemProcess


class EmployeeProfilePermissionPolicy(RecordPermissionPolicy):
    """Employee Profile Permission Policy class."""

    can_read = [AnyUser(), SystemProcess()]
    can_list = [AnyUser(), SystemProcess()]

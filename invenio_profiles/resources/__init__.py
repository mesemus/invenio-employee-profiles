"""Resources for users employee profiles."""

from .employee_profile.resource import EmployeeProfileResource
from .employee_profile.config import EmployeeProfileResourceConfig

__all__ = (
    "EmployeeProfileResource",
    "EmployeeProfileResourceConfig",
)

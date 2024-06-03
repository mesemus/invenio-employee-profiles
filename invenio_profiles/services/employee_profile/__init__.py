"""Services for users employee profiles."""

from .config import EmployeeProfileServiceConfig
from .service import EmployeeProfileService

__all__ = (
    "EmployeeProfileService",
    "EmployeeProfileServiceConfig",
)

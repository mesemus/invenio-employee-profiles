"""Errors for Employee Profiles."""


class EmployeeProfileError(Exception):
    """Base exception for Employee Profiles errors."""


class EmployeeProfileDoesNotExistError(EmployeeProfileError):
    """The provided set spec does not exist."""

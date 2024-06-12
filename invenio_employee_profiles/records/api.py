from invenio_records.dumpers import SearchDumper
from invenio_records.dumpers.indexedat import IndexedAtDumperExt
from invenio_records.dumpers.relations import RelationDumperExt
from invenio_records.systemfields import ModelRelation, RelationsField, ModelField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields import IndexField
from invenio_users_resources.records.api import UserAggregate, GetRecordResolver

from .models import EmployeeProfileModel


class DirectIdPID:
    """Helper emulate a PID field."""

    def __init__(self, id_field="id"):
        """Constructor."""
        self._id_field = id_field

    def __get__(self, record, owner=None):
        """Evaluate the property."""
        if record is None:
            return GetRecordResolver(owner)
        return DirectIdPID(getattr(record, self._id_field))


class EmployeeProfile(Record):

    model_cls = EmployeeProfileModel

    dumper = SearchDumper(
        extensions=[
            RelationDumperExt("relations"),
            IndexedAtDumperExt(),
        ]
    )

    # Systemfields
    index = IndexField(
        "invenio_employee_profiles-employee-profile-v1.0.0",
        search_alias="invenio_employee_profiles",
    )

    pid = DirectIdPID()

    active = ModelField("active")

    user_id = ModelField("user_id")

    relations = RelationsField(
        user=ModelRelation(
            UserAggregate,
            "user_id",
            "user",
            attrs=[
                "email",
                "username",
                "profile",
                "preferences",
                "active",
                "confirmed",
                "verified_at",
            ],
        )
    )


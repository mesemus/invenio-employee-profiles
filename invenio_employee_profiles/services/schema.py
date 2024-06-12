import marshmallow as ma
from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from invenio_users_resources.services.schemas import UserSchema

class EmployeeProfileSchema(InvenioBaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    email_address = ma.fields.Email()
    biography = ma.fields.String()
    profile_image = ma.fields.String()
    user = ma.fields.Nested(UserSchema, required=True)
    active = ma.fields.Boolean()

from invenio_records_resources.services.records.components import ServiceComponent

class EmployeeProfileServiceComponent(ServiceComponent):

    # store user identity only on create, ignore later
    def create(self, identity, *, record, data, **kwargs):
        # copy model fields from user input
        record.user_id = data["user"]["id"]
        record.active = data.get("active", True)

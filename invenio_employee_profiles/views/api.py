def create_blueprint(app):
    blueprint = app.extensions['invenio-employee-profiles'].resource.as_blueprint()
    blueprint.record_once(init)
    return blueprint


def init(state):
    app = state.app
    ext = app.extensions["invenio-employee-profiles"]

    # register service
    sregistry = app.extensions["invenio-records-resources"].registry
    sregistry.register(
        ext.service, service_id=ext.service.config.service_id
    )

    # Register indexer
    if hasattr(ext.service, "indexer"):
        iregistry = app.extensions["invenio-indexer"].registry
        iregistry.register(
            ext.service.indexer,
            indexer_id=ext.service.config.service_id,
        )

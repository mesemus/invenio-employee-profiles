#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""setup of employee profiles."""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "512bb8ae048c"
down_revision = None
branch_labels = ("invenio_profiles",)
depends_on = None


def upgrade():
    """Upgrade database."""
    pass


def downgrade():
    """Downgrade database."""
    pass

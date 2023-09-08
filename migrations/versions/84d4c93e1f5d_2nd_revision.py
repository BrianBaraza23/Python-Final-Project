"""2nd revision

Revision ID: 84d4c93e1f5d
Revises: 26f794c63ec7
Create Date: 2023-09-08 08:04:31.592130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84d4c93e1f5d'
down_revision: Union[str, None] = '26f794c63ec7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

"""corrected models code

Revision ID: 1a5f316580dc
Revises: cdde522d368f
Create Date: 2023-09-08 10:12:43.761845

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a5f316580dc'
down_revision: Union[str, None] = 'cdde522d368f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_actors',
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('actor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_actors')
    # ### end Alembic commands ###
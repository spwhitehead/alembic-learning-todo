"""add description and urgency columns

Revision ID: a53f60f9a76a
Revises: 921ede4cf10e
Create Date: 2024-04-15 16:50:44.830553

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel



# revision identifiers, used by Alembic.
revision: str = 'a53f60f9a76a'
down_revision: Union[str, None] = '921ede4cf10e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('task_description', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('task', sa.Column('urgency', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'urgency')
    op.drop_column('task', 'task_description')
    # ### end Alembic commands ###
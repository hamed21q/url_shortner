"""create url table

Revision ID: b845f48295d1
Revises: 
Create Date: 2024-06-18 06:37:31.016777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b845f48295d1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "urls",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("original_url", sa.String(length=256), nullable=False),
        sa.Column("hashed_url", sa.String(length=256), nullable=False, unique=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("original_url"),
    )


def downgrade() -> None:
    op.drop_table("urls")

"""create user table

Revision ID: dd32b411f250
Revises: 
Create Date: 2023-09-28 23:10:24.017644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = 'dd32b411f250'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True,
                  index=True, autoincrement=True),
        sa.Column("firstname", sa.String(255)),
        sa.Column("lastname", sa.String(255), nullable=True),
        sa.Column("roles", sa.String(255), nullable=True),
        sa.Column("status", sa.Integer),
        sa.Column("username", sa.String(20)),
        sa.Column("password_hashed", sa.String(255)),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    )


def downgrade() -> None:
    op.drop_table("user")

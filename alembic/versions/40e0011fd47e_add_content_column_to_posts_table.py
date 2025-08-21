"""add content column to posts table

Revision ID: 40e0011fd47e
Revises: c5951cc9a962
Create Date: 2025-08-21 11:15:59.680889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40e0011fd47e'
down_revision: Union[str, Sequence[str], None] = 'c5951cc9a962'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass

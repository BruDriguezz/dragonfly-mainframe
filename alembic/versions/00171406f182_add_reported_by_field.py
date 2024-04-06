"""Add reported_by field

Revision ID: 00171406f182
Revises: 7c8806e19b45
Create Date: 2023-06-13 16:07:42.065109

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "00171406f182"
down_revision = "7c8806e19b45"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("packages", sa.Column("reported_by", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("packages", "reported_by")
    # ### end Alembic commands ###

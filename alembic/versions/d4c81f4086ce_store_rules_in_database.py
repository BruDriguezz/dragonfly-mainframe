"""Store rules in database

Revision ID: d4c81f4086ce
Revises: c3f59638859f
Create Date: 2023-05-13 17:20:31.395329

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "d4c81f4086ce"
down_revision = "c3f59638859f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table("rules", sa.Column("name", sa.String(), nullable=False), sa.PrimaryKeyConstraint("name"))
    op.create_table(
        "package_rules",
        sa.Column("package_id", sa.UUID(), nullable=True),
        sa.Column("rule_name", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["package_id"],
            ["packages.package_id"],
        ),
        sa.ForeignKeyConstraint(
            ["rule_name"],
            ["rules.name"],
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("package_rules")
    op.drop_table("rules")
    # ### end Alembic commands ###
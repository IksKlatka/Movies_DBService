"""alter table movies

Revision ID: 387535a65ccd
Revises: cfa3fa52f951
Create Date: 2023-05-24 10:30:33.155894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '387535a65ccd'
down_revision = 'cfa3fa52f951'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
     ALTER TABLE movies
        ADD COLUMN budget int,
        ADD COLUMN popularity float,
        ADD COLUMN release_date date,
        ADD COLUMN revenue int;
     """)


def downgrade() -> None:
    op.execute("""
    ALTER TABLE movies
        DROP COLUMN budget,
        DROP COLUMN popularity,
        DROP COLUMN release_date,
        DROP COLUMN revenue;
    """)
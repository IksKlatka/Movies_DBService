"""alter table movies

Revision ID: 167164fc149e
Revises: bbb1b2a6e251
Create Date: 2023-05-20 15:50:39.986890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '167164fc149e'
down_revision = 'bbb1b2a6e251'
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
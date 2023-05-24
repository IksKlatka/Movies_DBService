"""create movie_keywords table

Revision ID: cfa3fa52f951
Revises: 87483bf737fb
Create Date: 2023-04-29 12:35:54.642699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfa3fa52f951'
down_revision = '87483bf737fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
        CREATE TABLE movie_keywords(
            movie_id INT references movies(movie_id) on delete cascade,
            keyword_id INT references keywords(keyword_id) on delete cascade
            );
    """)


def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS movie_keywords CASCADE; 
""")


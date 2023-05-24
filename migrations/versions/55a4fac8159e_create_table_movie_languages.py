"""create table movielanguages

Revision ID: 55a4fac8159e
Revises: b687107fac13
Create Date: 2023-04-24 08:16:05.569887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55a4fac8159e'
down_revision = 'b687107fac13'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql 
    CREATE TABLE movie_languages (
        movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
        lang_id VARCHAR(2) NOT NULL REFERENCES languages(lang_id) ON DELETE CASCADE
    );

""")


def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS movie_languages CASCADE;
""")

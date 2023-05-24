"""create table movie_countries

Revision ID: 74ffe47131fe
Revises: 6d2fdb7423c3
Create Date: 2023-04-28 16:12:14.720545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74ffe47131fe'
down_revision = '6d2fdb7423c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sQL
    CREATE TABLE movie_countries(
        movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
        country_id VARCHAR(3) REFERENCES countries(country_id) ON DELETE CASCADE

        );
""")


def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS movie_countries CASCADE;
""")
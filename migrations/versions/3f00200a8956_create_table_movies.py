"""create table movies

Revision ID: 3f00200a8956
Revises: 
Create Date: 2023-04-15 21:00:05.487548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f00200a8956'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql 
    CREATE TABLE movies(
        movie_id SERIAL PRIMARY KEY,
        title TEXT
    );
""")


def downgrade() -> None:
    op.execute(f"""
    --sql 
    DROP TABLE IF EXISTS movies CASCADE;
""")

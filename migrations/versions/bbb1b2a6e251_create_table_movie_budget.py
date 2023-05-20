"""create table movie_budget

Revision ID: bbb1b2a6e251
Revises: cfa3fa52f951
Create Date: 2023-05-20 12:17:25.737543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbb1b2a6e251'
down_revision = 'cfa3fa52f951'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql 
    CREATE TABLE movie_budget(
        movie_id INT,
        budget INT,
    
        CONSTRAINT fk_movie_id FOREIGN KEY (movie_id)
            REFERENCES movies(movie_id)
        );

""")


def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS movie_budget CASCADE;
""")

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
            movie_id INT,
            keyword_id INT,

            CONSTRAINT fk_movie_id FOREIGN KEY (movie_id)
                REFERENCES movies(movie_id),
            CONSTRAINT fk_keyword_id FOREIGN KEY (keyword_id)
                REFERENCES keyword(keyword_id)  
            );
    """)


def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS movie_keywords CASCADE; 
""")


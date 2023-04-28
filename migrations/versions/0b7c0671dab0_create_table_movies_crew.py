"""create table movies_crew

Revision ID: 0b7c0671dab0
Revises: 8f71ebd68947
Create Date: 2023-04-20 19:04:39.676890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b7c0671dab0'
down_revision = '8f71ebd68947'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute(f"""
    --sql
    CREATE TABLE movie_crew(
        movie_id INT,
        person_id INT,
        credit_id TEXT,
        department TEXT,
        job TEXT,
        gender INT,

        CONSTRAINT fk_movie_id FOREIGN KEY (movie_id)
            REFERENCES movies(movie_id),
        CONSTRAINT fk_person_id FOREIGN KEY (person_id)
            REFERENCES crew(person_id)      
    )

""")


def downgrade() -> None:
    op.execute(f"""
        DROP TABLE IF EXISTS movie_crew CASCADE;
    """)


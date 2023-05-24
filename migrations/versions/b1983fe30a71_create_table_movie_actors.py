"""create table movie_actors

Revision ID: b1983fe30a71
Revises: 6226dc28417c
Create Date: 2023-04-15 21:00:43.164680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1983fe30a71'
down_revision = '6226dc28417c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql
    CREATE TABLE movie_actors(
        movie_id int references movies(movie_id) on DELETE cascade,
        actor_id int references actors(actor_id) on DELETE cascade,
        cast_id     INT,
        character   TEXT,
        credit_id   TEXT, 
        gender      INT, 
        orders      INT    
         
    );
""")


def downgrade() -> None:
    op.execute(f"""
    --sql
    DROP TABLE movie_actors;
""")
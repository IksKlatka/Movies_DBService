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
        movie_id    INT,
        actor_id    INT, 
        cast_id     INT,
        character   TEXT,
        credit_id   TEXT, 
        gender      INT, 
        orders      INT,        
    
        CONSTRAINT fk_movie_id FOREIGN KEY (movie_id)
            REFERENCES movies(movie_id),
        CONSTRAINT fk_actor_id FOREIGN KEY (actor_id)
            REFERENCES actors(actor_id)            
    );
""")


def downgrade() -> None:
    op.execute(f"""
    --sql
    DROP TABLE movie_actors;
""")
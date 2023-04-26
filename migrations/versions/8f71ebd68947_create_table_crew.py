"""create table crew

Revision ID: 8f71ebd68947
Revises: b1983fe30a71
Create Date: 2023-04-20 19:03:12.200238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f71ebd68947'
down_revision = 'b1983fe30a71'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql 
    CREATE TABLE crew(
        person_id SERIAL PRIMARY KEY,
        name TEXT
    );
""")


def downgrade() -> None:
    op.execute(f"""
    --sql 
    DROP TABLE IF EXISTS crew CASCADE;
""")

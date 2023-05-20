"""create keywords table

Revision ID: 87483bf737fb
Revises: a22e8e043326
Create Date: 2023-04-29 12:35:42.311030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87483bf737fb'
down_revision = 'a22e8e043326'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.execute(f"""
    CREATE TABLE keywords(
        keyword_id SERIAL PRIMARY KEY NOT NULL,
        name TEXT        
        );
""")

def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS keywords CASCADE;
""")

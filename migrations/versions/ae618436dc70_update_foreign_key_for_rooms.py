"""update foreign key for rooms

Revision ID: ae618436dc70
Revises: fc6fd21278f1
Create Date: 2025-08-29 13:07:37.688329

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae618436dc70'
down_revision: Union[str, Sequence[str], None] = 'fc6fd21278f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Drop old foreign key
    op.drop_constraint('rooms_hotel_id_fkey', 'rooms', type_='foreignkey')
    # Add new foreign key
    op.create_foreign_key(
        'rooms_hotel_id_fkey',
        'rooms', 'hotel',
        ['hotel_id'], ['id']
    )

def downgrade():
    op.drop_constraint('rooms_hotel_id_fkey', 'rooms', type_='foreignkey')
    op.create_foreign_key(
        'rooms_hotel_id_fkey',
        'rooms', 'hotels',  # old table
        ['hotel_id'], ['id']
    )


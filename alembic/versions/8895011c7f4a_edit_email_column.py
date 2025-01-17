"""edit email Column

Revision ID: 8895011c7f4a
Revises: 4deaa875eec4
Create Date: 2024-09-18 04:12:52.546484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8895011c7f4a'
down_revision: Union[str, None] = '4deaa875eec4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_email_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    # ### end Alembic commands ###

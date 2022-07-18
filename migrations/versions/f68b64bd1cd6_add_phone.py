"""add phone

Revision ID: f68b64bd1cd6
Revises: 8fa6987b7932
Create Date: 2022-07-18 10:29:35.702449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f68b64bd1cd6'
down_revision = '8fa6987b7932'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone')
    # ### end Alembic commands ###

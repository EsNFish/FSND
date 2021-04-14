"""add missing items to artist

Revision ID: 170e9f5a7391
Revises: be5c3527c32d
Create Date: 2021-04-14 15:56:39.148815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '170e9f5a7391'
down_revision = 'be5c3527c32d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('looking_for_venues', sa.Boolean(), nullable=True))
    op.add_column('artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'seeking_description')
    op.drop_column('artist', 'looking_for_venues')
    # ### end Alembic commands ###
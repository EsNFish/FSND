"""change artist and venues genres to arrays isntead of other table

Revision ID: 20f5ddf86bfa
Revises: d38b7709be3f
Create Date: 2021-04-15 17:19:28.131418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20f5ddf86bfa'
down_revision = 'd38b7709be3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venuegenre')
    op.drop_table('artistgenre')
    op.add_column('artist', sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))
    op.add_column('venue', sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'genres')
    op.drop_column('artist', 'genres')
    op.create_table('artistgenre',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('genre', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='artistgenre_artist_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='artistgenre_pkey')
    )
    op.create_table('venuegenre',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('genre', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], name='venuegenre_venue_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='venuegenre_pkey')
    )
    # ### end Alembic commands ###

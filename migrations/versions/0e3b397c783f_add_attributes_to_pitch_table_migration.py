"""add attributes to pitch table migration

Revision ID: 0e3b397c783f
Revises: ceb4db1af893
Create Date: 2022-05-11 10:25:11.569731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e3b397c783f'
down_revision = 'ceb4db1af893'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('title', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'title')
    # ### end Alembic commands ###

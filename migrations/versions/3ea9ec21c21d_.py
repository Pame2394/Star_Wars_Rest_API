"""empty message

Revision ID: 3ea9ec21c21d
Revises: 3df52fb774ff
Create Date: 2021-04-19 05:49:34.873827

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3ea9ec21c21d'
down_revision = '3df52fb774ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planets', 'image_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('image_url', mysql.VARCHAR(length=250), nullable=False))
    # ### end Alembic commands ###

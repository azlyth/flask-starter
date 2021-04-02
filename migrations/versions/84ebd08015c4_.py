"""empty message

Revision ID: 84ebd08015c4
Revises: fb060a24643d
Create Date: 2021-04-02 13:36:11.979885

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '84ebd08015c4'
down_revision = 'fb060a24643d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('counter', 'count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('counter', sa.Column('count', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
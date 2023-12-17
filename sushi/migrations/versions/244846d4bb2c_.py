"""empty message

Revision ID: 244846d4bb2c
Revises: d9da38ed13b2
Create Date: 2023-12-16 17:42:41.181679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '244846d4bb2c'
down_revision = 'd9da38ed13b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo', sa.BLOB(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goods', schema=None) as batch_op:
        batch_op.drop_column('photo')

    # ### end Alembic commands ###

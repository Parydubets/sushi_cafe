"""empty message

Revision ID: 30dda6ca48d0
Revises: 244846d4bb2c
Create Date: 2023-12-17 19:50:12.215507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30dda6ca48d0'
down_revision = '244846d4bb2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goods', schema=None) as batch_op:
        batch_op.alter_column('photo',
               existing_type=sa.BLOB(),
               type_=sa.String(length=30),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goods', schema=None) as batch_op:
        batch_op.alter_column('photo',
               existing_type=sa.String(length=30),
               type_=sa.BLOB(),
               existing_nullable=False)

    # ### end Alembic commands ###

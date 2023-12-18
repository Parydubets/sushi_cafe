"""empty message

Revision ID: d5a8140e1df6
Revises: abfef3e8b46f
Create Date: 2023-12-18 01:30:29.475319

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd5a8140e1df6'
down_revision = 'abfef3e8b46f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('ix_user_age')
        batch_op.drop_index('ix_user_name')

    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('address', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('phone', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('ix_user_name', ['name'], unique=False)
        batch_op.create_index('ix_user_age', ['age'], unique=False)

    # ### end Alembic commands ###

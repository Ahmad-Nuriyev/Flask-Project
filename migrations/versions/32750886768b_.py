"""empty message

Revision ID: 32750886768b
Revises: 63a6abe260a9
Create Date: 2024-09-13 20:21:41.122407

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '32750886768b'
down_revision = '63a6abe260a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_products',
    sa.Column('user.id', sa.Integer(), nullable=True),
    sa.Column('product.id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product.id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user.id'], ['user.id'], )
    )
    op.drop_table('favorites')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorites',
    sa.Column('user.id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product.id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['product.id'], ['product.id'], name='favorites_ibfk_1'),
    sa.ForeignKeyConstraint(['user.id'], ['user.id'], name='favorites_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('user_products')
    # ### end Alembic commands ###

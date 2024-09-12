"""empty message

Revision ID: 1034a1b3bbf5
Revises: 5e1f4793c30f
Create Date: 2024-09-12 14:59:41.903882

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1034a1b3bbf5'
down_revision = '5e1f4793c30f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=mysql.INTEGER(),
               type_=sa.Float(),
               existing_nullable=False)
        batch_op.alter_column('discount_price',
               existing_type=mysql.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('discount_price',
               existing_type=sa.Float(),
               type_=mysql.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.Float(),
               type_=mysql.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###

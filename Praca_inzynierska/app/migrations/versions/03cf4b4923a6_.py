"""empty message

Revision ID: 03cf4b4923a6
Revises: 
Create Date: 2019-06-22 15:45:44.719389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03cf4b4923a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('balance',
    sa.Column('currency', sa.String(length=3), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Numeric(precision=10, scale=6), nullable=False),
    sa.Column('value_usd', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('currency', 'address', 'timestamp')
    )
    op.create_table('price',
    sa.Column('currency', sa.String(length=3), nullable=False),
    sa.Column('value_usd', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('currency', 'timestamp')
    )
    op.create_table('transfer',
    sa.Column('currency', sa.String(length=3), nullable=False),
    sa.Column('from_address', sa.String(length=100), nullable=False),
    sa.Column('to_address', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Numeric(precision=10, scale=6), nullable=False),
    sa.Column('transaction_id', sa.String(length=100), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('currency', 'transaction_id', 'timestamp')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transfer')
    op.drop_table('price')
    op.drop_table('balance')
    # ### end Alembic commands ###

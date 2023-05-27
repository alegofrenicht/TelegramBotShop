"""empty message

Revision ID: a80d9e1e1600
Revises: 9340c7838ca8
Create Date: 2023-05-25 15:32:36.761615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a80d9e1e1600'
down_revision = '9340c7838ca8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('device', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'telegram_user', ['owner'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('device', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('owner')

    # ### end Alembic commands ###

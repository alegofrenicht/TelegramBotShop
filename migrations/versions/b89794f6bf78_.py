"""empty message

Revision ID: b89794f6bf78
Revises: ed54a1e78322
Create Date: 2023-05-27 19:17:06.880439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b89794f6bf78'
down_revision = 'ed54a1e78322'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('telegram_user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('chat_id', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('telegram_user', schema=None) as batch_op:
        batch_op.drop_column('chat_id')

    # ### end Alembic commands ###

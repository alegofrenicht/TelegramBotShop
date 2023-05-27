"""empty message

Revision ID: 282c954f9413
Revises: 28ff007d5656
Create Date: 2023-05-21 19:42:07.898317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '282c954f9413'
down_revision = '28ff007d5656'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('device', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=240), nullable=True))
        batch_op.create_index(batch_op.f('ix_device_description'), ['description'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('device', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_device_description'))
        batch_op.drop_column('description')

    # ### end Alembic commands ###

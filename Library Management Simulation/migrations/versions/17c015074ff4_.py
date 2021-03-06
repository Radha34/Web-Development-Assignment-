"""empty message

Revision ID: 17c015074ff4
Revises: 768a31fb0a7e
Create Date: 2021-05-16 22:59:34.334271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17c015074ff4'
down_revision = '768a31fb0a7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teachers', 'id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('teachers', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teachers', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('teachers', 'id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###

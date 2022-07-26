"""Initial migration.

Revision ID: 689ca658a899
Revises: 
Create Date: 2022-07-25 14:36:32.246421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '689ca658a899'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('contact', sa.String(length=11), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('contact'),
    sa.UniqueConstraint('username')
    )
    op.create_table('project',
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('pname', sa.String(length=50), nullable=False),
    sa.Column('desc', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('pid'),
    sa.UniqueConstraint('desc'),
    sa.UniqueConstraint('pname')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    op.drop_table('user')
    # ### end Alembic commands ###

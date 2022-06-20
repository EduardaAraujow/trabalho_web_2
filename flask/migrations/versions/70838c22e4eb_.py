"""empty message

Revision ID: 70838c22e4eb
Revises: 
Create Date: 2022-04-13 12:13:56.516603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70838c22e4eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('controller',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('action_id', sa.Integer(), nullable=False),
    sa.Column('controller_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['action_id'], ['action.id'], ),
    sa.ForeignKeyConstraint(['controller_id'], ['controller.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('privilege',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('allow_boolean', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('role_id', 'resource_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('privilege')
    op.drop_table('user')
    op.drop_table('resource')
    op.drop_table('role')
    op.drop_table('controller')
    op.drop_table('action')
    # ### end Alembic commands ###
"""empty message

Revision ID: 61e2fa43da05
Revises: 8af059107607
Create Date: 2017-05-01 06:09:19.637417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61e2fa43da05'
down_revision = '8af059107607'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('client_id', sa.String(length=40), nullable=False),
    sa.Column('client_secret', sa.String(length=55), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('description', sa.String(length=400), nullable=True),
    sa.Column('is_confidential', sa.Boolean(), nullable=True),
    sa.Column('_redirect_uris', sa.Text(), nullable=True),
    sa.Column('_default_scopes', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('client_id')
    )
    op.create_index(op.f('ix_clients_client_secret'), 'clients', ['client_secret'], unique=True)
    op.create_table('grants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.String(length=40), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('redirect_uri', sa.String(length=255), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.Column('_scopes', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.client_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_grants_code'), 'grants', ['code'], unique=False)
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.String(length=40), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('token_type', sa.String(length=40), nullable=True),
    sa.Column('access_token', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.Column('_scopes', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['clients.client_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('access_token'),
    sa.UniqueConstraint('refresh_token')
    )
    op.add_column(u'users', sa.Column('created', sa.DateTime(), nullable=False))
    op.add_column(u'users', sa.Column('updated', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'users', 'updated')
    op.drop_column(u'users', 'created')
    op.drop_table('tokens')
    op.drop_index(op.f('ix_grants_code'), table_name='grants')
    op.drop_table('grants')
    op.drop_index(op.f('ix_clients_client_secret'), table_name='clients')
    op.drop_table('clients')
    # ### end Alembic commands ###

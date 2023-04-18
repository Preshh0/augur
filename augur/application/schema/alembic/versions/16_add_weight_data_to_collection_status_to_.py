"""Add weight data to collection status to determine collection order of repos

Revision ID: 16
Revises: 15
Create Date: 2023-04-10 18:28:12.460522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16'
down_revision = '15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collection_status', sa.Column('core_weight', sa.BigInteger()), schema='augur_operations')
    op.add_column('collection_status', sa.Column('facade_weight', sa.BigInteger()), schema='augur_operations')
    op.add_column('collection_status', sa.Column('secondary_weight', sa.BigInteger()), schema='augur_operations')

    op.add_column('collection_status', sa.Column('issue_pr_sum', sa.BigInteger()), schema='augur_operations')
    op.add_column('collection_status', sa.Column('commit_sum', sa.BigInteger()), schema='augur_operations')

    op.drop_constraint('collection_status_repo_id_fk', 'collection_status', schema='augur_operations', type_='foreignkey')
    op.create_foreign_key('collection_status_repo_id_fk', 'collection_status', 'repo', ['repo_id'], ['repo_id'], source_schema='augur_operations', referent_schema='augur_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('collection_status_repo_id_fk', 'collection_status', schema='augur_operations', type_='foreignkey')
    op.create_foreign_key('collection_status_repo_id_fk', 'collection_status', 'repo', ['repo_id'], ['repo_id'], source_schema='augur_operations')
    op.drop_column('collection_status', 'facade_weight', schema='augur_operations')
    op.drop_column('collection_status', 'core_weight', schema='augur_operations')
    # ### end Alembic commands ###

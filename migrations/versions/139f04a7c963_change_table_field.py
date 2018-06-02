"""change table field

Revision ID: 139f04a7c963
Revises: cd4c82b55e5b
Create Date: 2018-06-02 13:42:47.974897

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '139f04a7c963'
down_revision = 'cd4c82b55e5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('job_ibfk_2', 'job', type_='foreignkey')
    op.drop_constraint('job_ibfk_1', 'job', type_='foreignkey')
    op.create_foreign_key(None, 'job', 'company_detail', ['company_id'], ['id'], ondelete='CASCADE')
    op.drop_column('job', 'applicants_id')
    op.add_column('user', sa.Column('real_name', sa.String(length=32), nullable=True))
    op.drop_column('user', 'realname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('realname', mysql.VARCHAR(length=32), nullable=True))
    op.drop_column('user', 'real_name')
    op.add_column('job', sa.Column('applicants_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'job', type_='foreignkey')
    op.create_foreign_key('job_ibfk_1', 'job', 'user', ['applicants_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key('job_ibfk_2', 'job', 'user', ['company_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###

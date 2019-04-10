"""adds categories

Revision ID: a113bcc9572e
Revises: 4f2a05d983af
Create Date: 2019-04-10 01:20:09.767062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a113bcc9572e'
down_revision = '4f2a05d983af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('category_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.add_column('moves', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key("fk_moves_categories", 'moves', 'categories', ['category_id'], ['category_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("fk_moves_categories", 'moves', type_='foreignkey')
    op.drop_column('moves', 'category_id')
    op.drop_table('categories')
    # ### end Alembic commands ###

"""empty message

Revision ID: d5062391d10a
Revises: 
Create Date: 2024-04-29 09:38:47.863117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5062391d10a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conta',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('saldo', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('conta')
    # ### end Alembic commands ###

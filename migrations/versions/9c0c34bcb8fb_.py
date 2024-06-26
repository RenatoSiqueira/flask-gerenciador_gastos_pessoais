"""empty message

Revision ID: 9c0c34bcb8fb
Revises: d5062391d10a
Create Date: 2024-04-29 19:48:01.669358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c0c34bcb8fb'
down_revision = 'd5062391d10a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transacao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.Column('tipo', sa.Enum('entrada', 'saida', name='tipoenum'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transacao')
    # ### end Alembic commands ###

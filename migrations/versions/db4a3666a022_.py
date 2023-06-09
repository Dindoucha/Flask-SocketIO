"""empty message

Revision ID: db4a3666a022
Revises: 9de06034a491
Create Date: 2023-03-28 12:06:48.521802

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'db4a3666a022'
down_revision = '9de06034a491'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('last_login', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=50),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['username'])
        batch_op.create_unique_constraint(None, ['email'])

    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.drop_constraint('game_player_two_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('game_result_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('game_player_one_id_fkey', type_='foreignkey')

    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.drop_constraint('player_game_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('player_player_id_fkey', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.create_foreign_key('player_player_id_fkey', 'account', ['player_id'], ['id'])
        batch_op.create_foreign_key('player_game_id_fkey', 'game', ['game_id'], ['id'])

    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.create_foreign_key('game_player_one_id_fkey', 'account', ['player_one_id'], ['id'])
        batch_op.create_foreign_key('game_result_id_fkey', 'result', ['result_id'], ['id'])
        batch_op.create_foreign_key('game_player_two_id_fkey', 'account', ['player_two_id'], ['id'])

    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('password',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.drop_column('last_login')
        batch_op.drop_column('created_on')

    # ### end Alembic commands ###

"""Create stock_data and linear_regression_predictions tables

Revision ID: 60269a665a4a
Revises: 
Create Date: 2024-07-21 21:42:19.224189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60269a665a4a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('linear_regression_predictions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('prediction_date', sa.DateTime(), nullable=True),
    sa.Column('predicted_close', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_linear_regression_predictions_id'), 'linear_regression_predictions', ['id'], unique=False)
    op.create_index(op.f('ix_linear_regression_predictions_prediction_date'), 'linear_regression_predictions', ['prediction_date'], unique=False)
    op.create_index(op.f('ix_linear_regression_predictions_ticker'), 'linear_regression_predictions', ['ticker'], unique=False)
    op.create_table('stock_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('open', sa.Float(), nullable=True),
    sa.Column('high', sa.Float(), nullable=True),
    sa.Column('low', sa.Float(), nullable=True),
    sa.Column('close', sa.Float(), nullable=True),
    sa.Column('volume', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stock_data_date'), 'stock_data', ['date'], unique=False)
    op.create_index(op.f('ix_stock_data_id'), 'stock_data', ['id'], unique=False)
    op.create_index(op.f('ix_stock_data_ticker'), 'stock_data', ['ticker'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stock_data_ticker'), table_name='stock_data')
    op.drop_index(op.f('ix_stock_data_id'), table_name='stock_data')
    op.drop_index(op.f('ix_stock_data_date'), table_name='stock_data')
    op.drop_table('stock_data')
    op.drop_index(op.f('ix_linear_regression_predictions_ticker'), table_name='linear_regression_predictions')
    op.drop_index(op.f('ix_linear_regression_predictions_prediction_date'), table_name='linear_regression_predictions')
    op.drop_index(op.f('ix_linear_regression_predictions_id'), table_name='linear_regression_predictions')
    op.drop_table('linear_regression_predictions')
    # ### end Alembic commands ###
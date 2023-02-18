"""improved photometric series

Revision ID: c276f6343274
Revises: dbbeed743db3
Create Date: 2023-02-15 09:43:14.121584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c276f6343274'
down_revision = 'dbbeed743db3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'photometric_series', sa.Column('series_name', sa.String(), nullable=False)
    )
    op.add_column(
        'photometric_series', sa.Column('channel', sa.String(), nullable=False)
    )
    op.add_column(
        'photometric_series', sa.Column('mag_first', sa.Float(), nullable=False)
    )
    op.add_column(
        'photometric_series', sa.Column('mag_last', sa.Float(), nullable=False)
    )
    op.add_column(
        'photometric_series', sa.Column('mag_last_detected', sa.Float(), nullable=True)
    )
    op.add_column(
        'photometric_series', sa.Column('median_snr', sa.Float(), nullable=True)
    )
    op.add_column(
        'photometric_series', sa.Column('best_snr', sa.Float(), nullable=True)
    )
    op.add_column(
        'photometric_series', sa.Column('worst_snr', sa.Float(), nullable=True)
    )
    op.add_column(
        'photometric_series', sa.Column('autodelete', sa.Boolean(), nullable=False)
    )
    op.alter_column(
        'photometric_series',
        'mjd_last_detected',
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=True,
    )
    op.drop_index(
        'ix_photometric_series_series_identifier', table_name='photometric_series'
    )
    op.drop_constraint(
        'photometric_series_hash_key', 'photometric_series', type_='unique'
    )
    op.drop_index('ix_photometric_series_filename', table_name='photometric_series')
    op.create_index(
        op.f('ix_photometric_series_filename'),
        'photometric_series',
        ['filename'],
        unique=True,
    )
    op.create_index(
        op.f('ix_photometric_series_best_snr'),
        'photometric_series',
        ['best_snr'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_channel'),
        'photometric_series',
        ['channel'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_exp_time'),
        'photometric_series',
        ['exp_time'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_filter'),
        'photometric_series',
        ['filter'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_frame_rate'),
        'photometric_series',
        ['frame_rate'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_hash'), 'photometric_series', ['hash'], unique=True
    )
    op.create_index(
        op.f('ix_photometric_series_mag_first'),
        'photometric_series',
        ['mag_first'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_mag_last'),
        'photometric_series',
        ['mag_last'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_mag_last_detected'),
        'photometric_series',
        ['mag_last_detected'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_maxima'),
        'photometric_series',
        ['maxima'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_mean_mag'),
        'photometric_series',
        ['mean_mag'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_median_snr'),
        'photometric_series',
        ['median_snr'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_medians'),
        'photometric_series',
        ['medians'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_minima'),
        'photometric_series',
        ['minima'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_num_exp'),
        'photometric_series',
        ['num_exp'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_rms_mag'),
        'photometric_series',
        ['rms_mag'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_series_name'),
        'photometric_series',
        ['series_name'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_series_obj_id'),
        'photometric_series',
        ['series_obj_id'],
        unique=False,
    )
    op.create_index(
        op.f('ix_photometric_series_stds'), 'photometric_series', ['stds'], unique=False
    )
    op.create_index(
        op.f('ix_photometric_series_worst_snr'),
        'photometric_series',
        ['worst_snr'],
        unique=False,
    )
    op.create_index(
        'phot_series_deduplication_index',
        'photometric_series',
        [
            'obj_id',
            'instrument_id',
            'origin',
            'filter',
            'series_name',
            'series_obj_id',
            'channel',
        ],
        unique=True,
    )
    op.drop_column('photometric_series', 'upload_id')
    op.drop_column('photometric_series', 'series_identifier')
    op.drop_column('photometric_series', 'channel_id')
    # ### end Alembic commands ###

    op.execute(
        'alter table "public"."photometric_series" alter column "origin" drop default;'
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'photometric_series',
        sa.Column('channel_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.add_column(
        'photometric_series',
        sa.Column(
            'series_identifier', sa.VARCHAR(), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        'photometric_series',
        sa.Column('upload_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_index('phot_series_deduplication_index', table_name='photometric_series')
    op.drop_index(
        op.f('ix_photometric_series_worst_snr'), table_name='photometric_series'
    )
    op.drop_index(op.f('ix_photometric_series_stds'), table_name='photometric_series')
    op.drop_index(
        op.f('ix_photometric_series_series_obj_id'), table_name='photometric_series'
    )
    op.drop_index(
        op.f('ix_photometric_series_series_name'), table_name='photometric_series'
    )
    op.drop_index(
        op.f('ix_photometric_series_rms_mag'), table_name='photometric_series'
    )
    op.drop_index(
        op.f('ix_photometric_series_num_exp'), table_name='photometric_series'
    )
    op.drop_index(op.f('ix_photometric_series_minima'), table_name='photometric_series')
    op.drop_index(
        op.f('ix_photometric_series_medians'), table_name='photometric_series'
    )
    op.drop_index(
        op.f('ix_photometric_series_median_snr'), table_name='photometric_series'
    )
    op.drop_index(
        op.f('ix_photometric_series_mean_mag'), table_name='photometric_series'
    )
    op.drop_index(op.f('ix_photometric_series_maxima'), table_name='photometric_series')
    op.drop_index(
        op.f('ix_photometric_series_mag_last_detected'), table_name='photometric_series'
    )
    op.drop_index(
        op.f('ix_photometric_series_mag_last'), table_name='photometric_series'
    )
    op.drop_index(
        op.f('ix_photometric_series_mag_first'), table_name='photometric_series'
    )
    op.drop_index(op.f('ix_photometric_series_hash'), table_name='photometric_series')
    op.drop_index(
        op.f('ix_photometric_series_frame_rate'), table_name='photometric_series'
    )
    op.drop_index(op.f('ix_photometric_series_filter'), table_name='photometric_series')
    op.drop_index(
        op.f('ix_photometric_series_exp_time'), table_name='photometric_series'
    )
    op.drop_index(
        op.f('ix_photometric_series_channel'), table_name='photometric_series'
    )
    op.drop_index(
        op.f('ix_photometric_series_best_snr'), table_name='photometric_series'
    )
    op.drop_index(
        op.f('ix_photometric_series_filename'), table_name='photometric_series'
    )
    op.create_index(
        'ix_photometric_series_filename',
        'photometric_series',
        ['filename'],
        unique=False,
    )
    op.create_unique_constraint(
        'photometric_series_hash_key', 'photometric_series', ['hash']
    )
    op.create_index(
        'ix_photometric_series_series_identifier',
        'photometric_series',
        ['series_identifier'],
        unique=False,
    )
    op.alter_column(
        'photometric_series',
        'mjd_last_detected',
        existing_type=sa.DOUBLE_PRECISION(precision=53),
        nullable=False,
    )
    op.drop_column('photometric_series', 'autodelete')
    op.drop_column('photometric_series', 'worst_snr')
    op.drop_column('photometric_series', 'best_snr')
    op.drop_column('photometric_series', 'median_snr')
    op.drop_column('photometric_series', 'mag_last_detected')
    op.drop_column('photometric_series', 'mag_last')
    op.drop_column('photometric_series', 'mag_first')
    op.drop_column('photometric_series', 'channel')
    op.drop_column('photometric_series', 'series_name')
    # ### end Alembic commands ###

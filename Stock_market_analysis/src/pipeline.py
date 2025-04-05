import pandas as pd
from data_cleaning import clean_data
from eda import summary_statistics ,top_n_stockprices , structure
from visualization import preprocess_data, plot_closing_price, plot_correlation_heatmap ,plot_close_distribution, plot_volume
from moving_average import moving_average


def run_data_pipeline(input_file_path, output_file_path):
    clean_data(input_file_path, output_file_path)
    df = pd.read_parquet(output_file_path)
    # df_st = structure(df)
    summary = summary_statistics(df)
    top, bottom = top_n_stockprices(df)
    moving_avg = moving_average(df)
    return df, summary, top, bottom,moving_avg



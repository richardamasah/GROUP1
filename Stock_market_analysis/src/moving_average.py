def moving_average(df, column='close', window=200):
     return df[column].rolling(window=window).mean()
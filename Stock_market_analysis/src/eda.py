
#Data Exploration

def structure(df):
    print("First 5 rows")
    print(df.head())

    print("Checking for null values")
    print(df.isnull().sum())

    print("checking for duplicates")
    print(df.duplicated().sum())

    print("Shape of data")
    print(df.shape)

    print("Total rows: ", df.shape[0])
    print("Total columns: ", df.shape[1])

def summary_statistics(df):
    '''
    - The Close price (final price of the stock at the end of each trading day) has a mean of 713,161 with a standard deviation of 146,252,100. This suggests that stock prices exhibit significant fluctuations over time, indicating market volatility.

- The mean Open price is 716,707, while the mean Close price is 713,161. This suggests that stock prices do not drastically change from market opening to closing, on average.

- The mean High price (maximum price reached in a day) is 734,470, The mean Low price (minimum price in a day) is 695,959.
This indicates that during a typical trading day, prices fluctuate by approximately 38,511 units on average.

- The mean trading Volume is 1.10 million shares per day, with a standard deviation of 13.12 million.
The lowest daily Volume recorded was 0,
The highest was 18 billion shares, suggesting extreme variations in trading activity, possibly due to major market events or company-specific announcements.


- 25% of the trading days had a Close price below 6.5, indicating that stock prices were lower for a quarter of the observed period.

- The median Close price is 14.32, meaning half of the trading days had Close prices below this value.

- 75% of days had Close prices below 28.13, meaning only a quarter of the trading days experienced significantly high prices.

- The dataset spans from January 2, 1962, to April 2, 2020, covering nearly 58 years of stock market data.

- The mean date is approximately September 25, 2006, which suggests that the dataset is balanced around the mid-2000s.
    '''
    return df.describe()

    

def top_n_stockprices(df, n=5):
    top = df.nlargest(n, 'close')
    bottom = df.nsmallest(n, 'close')
    return top, bottom
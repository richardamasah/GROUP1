#import dependencies and packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_stock_data(path):
    return pd.read_csv(path)

# Clean & preprocess the dataset
def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    return df

# Plot line chart of closing prices
def plot_closing_price(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.title('Stock Closing Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Correlation heatmap
def plot_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include='number')
    corr = numeric_df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()
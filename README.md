# GROUP 1 - PROJECT 1

# Stock Price Analysis Project

A collaborative project to analyze historical stock prices by building a complete data pipeline — from data collection to visualization and testing.

---
## About Dataset
### Overview
This dataset contains historical daily prices for all tickers currently trading on NASDAQ. The up to date list is available from nasdaqtrader.com. The historic data is retrieved from Yahoo finance via yfinance python package.

It contains prices for up to 01 of April 2020. If you need more up to date data, just fork and re-run data collection script also available from Kaggle.

Data Structure
The date for every symbol is saved in CSV format with common fields:

- Date - specifies trading date
- Open - opening price
- High - maximum price during the day
- Low - minimum price during the day
- Close - close price adjusted for splits
- Adj Close - adjusted close price adjusted for both dividends and splits.
- Volume - the number of shares that changed hands during a given day


---

## Data Pipeline Workflow

### Data Collection
- We use the `yfinance` library to download stock price data.
- Collected data includes Open, High, Low, Close, Adj Close, and Volume.

### Data Cleaning
- Removes:
  - Rows with missing (`NaN`) values
  - Duplicate records
- Converts date columns to `datetime` format

### Feature Engineering
- Calculates:
  - Moving averages (e.g., 5-day, 20-day)
  - Daily returns
- Adds technical indicators (optional)

### Correlation Analysis
- Computes Pearson correlation between the daily returns of different stocks
- Helps understand how stocks move in relation to each other

### Data Visualization
- Line plots of closing prices and moving averages
- Correlation heatmap of returns
- Trend comparisons across stocks

---

## Running The Project

1. Clone the repository:
```bash
git clone https://github.com/richardamasah/GROUP1.git
cd Stock_market_analysis
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Unit Testing

We use `unittest` to verify:
- Data cleaning logic (e.g., removal of NaNs and duplicates)
- Moving average calculations
- Edge case handling (e.g., short series)

Run tests using:

```bash
python -m unittest discover tests

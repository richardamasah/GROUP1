import unittest 
import pandas as pd
from src.moving_average import moving_average

class TestStockFunctions(unittest.TestCase):
    def test_moving_average(self):
        stock_prices = pd.DataFrame({
            'close': [100, 200, 300, 400, 500]
        })
        result = moving_average(stock_prices, column='close', window=3)
        expected_output = pd.Series([None, None, 200.0, 300.0, 400.0])
        pd.testing.assert_series_equal(result.reset_index(drop=True), expected_output, check_names=False)

    def test_insufficient_moving_average(self):
        stock_prices = pd.DataFrame({
            'date': ['2024-01-01', '2024-01-02'],
            'close': [150, 152]
        })

        result = moving_average(stock_prices, column='close', window=3)
        self.assertTrue(result.isna().all(), 'Should return NaN values when data is insufficient for moving average')

if __name__=='__main':
    unittest.main()
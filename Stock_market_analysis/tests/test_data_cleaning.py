import unittest
import pandas as pd
import os
import sys
from pathlib import Path
import shutil
import tempfile
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from src.data_cleaning import clean_data

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.output_file = os.path.join(self.test_dir, 'cleaned_data.parquet')

        # Create sample CSV files for testing
        self.sample_data1 = pd.DataFrame({
            'Date': ['1980-12-12', '1980-12-15', '1980-12-16', '1980-12-17', '1980-12-18'],
            'Open': [0.513393, 0.488839, 0.453125, 0.462054, 0.506696],
            'High': [0.515625, 0.488839, 0.458307, 0.467679, 0.508929],
            'Low': [0.513393, 0.486607, 0.453125, 0.462054, 0.506696],
            'Close': [0.513393, 0.486607, 0.453125, 0.462054, 0.506696],
            'Adj Close': [0.467682, 0.442857, 0.412500, 0.420536, 0.460714],
            'Volume': [11725800, 43971200, 26432000, 21610400, 18362400]
        })
        
        self.sample_data2 = pd.DataFrame({
            'Date': ['1980-12-12', '1980-12-15', '1980-12-16', '1980-12-17', '1980-12-18'],
            'Open': [0.513393, 0.488839, 0.453125, 0.462054, 50.0000], 
            'High': [0.515625, 0.488839, 0.458307, 0.467679, 51.0000],  
            'Low': [0.513393, 0.486607, 0.453125, 0.462054, 49.0000],   
            'Close': [0.513393, 0.486607, 0.453125, 0.462054, 50.5000], 
            'Adj Close': [0.467682, 0.442857, 0.412500, 0.420536, 45.0000],
            'Volume': [11725800, 43971200, 26432000, 21610400, 18362400]
        })

        # Save sample data to CSV files
        self.csv_file1 = os.path.join(self.test_dir, 'stock1.csv')
        self.csv_file2 = os.path.join(self.test_dir, 'stock2.csv')
        self.sample_data1.to_csv(self.csv_file1, index=False)
        self.sample_data2.to_csv(self.csv_file2, index=False)

    def tearDown(self):
        # Remove the temporary directory and its contents
        shutil.rmtree(self.test_dir)

    def test_clean_data_basic_functionality(self):
        # Run the data cleaning function
        df = clean_data(self.test_dir, self.output_file)

        # Check if the output file is created
        self.assertTrue(os.path.exists(self.output_file))

        # Check if the DataFrame is returned
        self.assertIsInstance(df, pd.DataFrame)

        # Check if columns are standardized
        self.assertTrue(all(col.islower() for col in df.columns))
        self.assertIn('symbol', df.columns)
        self.assertIn('stock1', df['symbol'].values)
        self.assertIn('stock2', df['symbol'].values)

    def test_date_conversion(self):
        # Run the data cleaning function
        df = clean_data(self.test_dir, self.output_file)

        # Check if 'Date' column is in datetime format
        self.assertEqual(df['date'].dtype, 'datetime64[ns]')

    def test_outlier_removal(self):
        # Test if outliers are properly removed
        df = clean_data(self.test_dir, self.output_file)
        
        # Stock2 had a value of 500 which should be removed as an outlier
        stock2_data = df[df['symbol'] == 'stock2']
        self.assertFalse(any(stock2_data['open'] > 30))

    def test_missing_directory(self):
        # Test for missing directory
        with self.assertRaises(FileNotFoundError):
            clean_data('/stocksdata/stocks', self.output_file)

    def test_empty_directory(self):
        # Create a temporary empty directory
        empty_dir = tempfile.mkdtemp()
        with self.assertRaises(FileNotFoundError):
            clean_data(empty_dir, self.output_file)
        shutil.rmtree(empty_dir)

if __name__ == '__main__':
    unittest.main()


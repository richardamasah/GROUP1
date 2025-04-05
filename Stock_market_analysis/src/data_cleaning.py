# src/data_cleaning.py
import pandas as pd
import os
from pathlib import Path

def clean_data(input_dir, output_path):
    """
    Clean multiple CSV files from a directory and combine them into a single parquet file.
    
    Args:
        input_dir (str): Directory containing CSV files
        output_path (str): Path to save the cleaned parquet file
    Returns:
        pd.DataFrame: Combined cleaned DataFrame
    """
    # Convert paths to Path objects
    input_dir = Path(input_dir)
    output_path = Path(output_path)
    
    print(f"📂 Looking for CSV files in: {input_dir}")
    
    # List to store all dataframes
    all_dfs = []
    
    # Get all CSV files in the directory
    csv_files = list(input_dir.glob('*.csv'))
    
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {input_dir}")
    
    print(f"✅ Found {len(csv_files)} CSV file(s). Starting cleaning process...")

    # Process each CSV file
    for file_path in csv_files:
        print(f"🔄 Processing: {file_path.name}")
        
        # Read the CSV
        df = pd.read_csv(file_path)
        
        # Convert 'Date' to datetime
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Handle missing values (forward fill)
        df.ffill(inplace=True)
        
        # Remove outliers (prices beyond 3 standard deviations)
        for col in ['Open', 'High', 'Low', 'Close']:
            if col in df.columns:  # Check if column exists
                mean = df[col].mean()
                std = df[col].std()
                df = df[(df[col] >= mean - 3 * std) & (df[col] <= mean + 3 * std)]
        
        # Standardize column names
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        
        # Optional: Add a column with the stock symbol from filename
        df['symbol'] = file_path.stem  # Gets filename without extension
        
        all_dfs.append(df)
    
    # Combine all dataframes
    combined_df = pd.concat(all_dfs, ignore_index=True)
    
    # Save to parquet
    combined_df.to_parquet(output_path, engine='pyarrow', index=False)

    print(f"🎉 Successfully cleaned and saved data to: {output_path.resolve()}")
    
    return combined_df

# Usage example
input_dir = 'data/stocks'
output_path = 'data/cleaned-stocks.parquet'

# Call the function
df = clean_data(input_dir, output_path)

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

        # Standardize column names
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        
        # Convert 'Date' to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Handle missing values (forward fill)
        df.ffill(inplace=True)


        #Remove outliers using IQR method
        price_cols = [col for col in ['open', 'high', 'low', 'close'] if col in df.columns]
        if price_cols:
            mask = True
            for col in price_cols:
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                mask &= (df[col] >= lower_bound) & (df[col] <= upper_bound)
            df = df[mask]

        df['symbol'] = file_path.stem  # Gets filename without extension
        all_dfs.append(df)
    
    # Combine all dataframes
    combined_df = pd.concat(all_dfs, ignore_index=True)

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save to parquet
    combined_df.to_parquet(output_path, engine='pyarrow', index=False)
    print(f"🎉 Successfully cleaned and saved data to: {output_path.resolve()}")

    return combined_df

if __name__ == '__main__':
    # Usage example
    input_dir = 'Stock_market_analysis/data/stocks'
    output_path = 'Stock_market_analysis/data/cleaned-stocks.parquet'
    df = clean_data(input_dir, output_path)


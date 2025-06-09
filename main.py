import pandas as pd
import os
import csv
from typing import List


def load_csv_files(data_dir: str) -> List[pd.DataFrame]:
    """
    Load and filter CSV files for Pink Morsel sales.
    Args:
        data_dir (str): Path to the folder containing CSV files.
        Returns:
        List[pd.DataFrame]: List of filtered DataFrames.
    """
    data_frames = []
    for file_name in os.listdir(data_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(data_dir, file_name)
            df = pd.read_csv(file_path)

            # Filter only Pink Morsels
            pink_morsels = df[df['product'] == 'Pink Morsel'].copy()

            # Calculate sales
            pink_morsels['Sales'] = pink_morsels['quantity'] * pink_morsels['price']

            # Keep only relevant columns
            filtered = pink_morsels[['Sales', 'date', 'region']]
            data_frames.append(filtered)

    return data_frames


def save_combined_data(data_frames: List[pd.DataFrame],
                       output_file: str) -> None:
   """
    Combine all DataFrames and save to a single CSV file.

    Args:
        data_frames (List[pd.DataFrame]): List of cleaned DataFrames.
        output_file (str): Path to the output CSV file.
    """
    combined_df = pd.concat(data_frames, ignore_index=True)
    combined_df.to_csv(output_file, index=False)
    print(f"✅ Output saved to {output_file}")


def main() -> None:
    """
    Main function to execute the data processing pipeline.
    """
    data_dir = 'data'
    output_file = 'formatted_sales_data.csv'
    filtered_data = load_csv_files(data_dir)
    save_combined_data(filtered_data, output_file)

        
if __name__ == '__main__':
    main()

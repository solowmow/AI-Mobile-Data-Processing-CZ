# data_cleaning.py

import pandas as pd

def load_data(file_path):
    """
    Load the dataset from the given file path.
    """
    try:
        data = pd.read_csv(file_path)  # Assuming CSV format, change accordingly
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def remove_duplicates(data):
    """
    Remove duplicate rows from the dataset.
    """
    cleaned_data = data.drop_duplicates()
    return cleaned_data

def handle_missing_values(data):
    """
    Handle missing values in the dataset.
    For simplicity, this example replaces missing values with 0.
    """
    cleaned_data = data.fillna(0)
    return cleaned_data

def remove_outliers(data, threshold=3):
    """
    Remove outliers from the dataset using a Z-score threshold.
    """
    z_scores = ((data - data.mean()) / data.std()).abs()
    cleaned_data = data[(z_scores < threshold).all(axis=1)]
    return cleaned_data

if __name__ == "__main__":
    # Example usage
    file_path = "your_data.csv"  # Replace with your dataset path
    data = load_data(file_path)

    if data is not None:
        cleaned_data = remove_duplicates(data)
        cleaned_data = handle_missing_values(cleaned_data)
        cleaned_data = remove_outliers(cleaned_data)

        # Save cleaned data to a new CSV file
        cleaned_data.to_csv("cleaned_data.csv", index=False)
        print("Data cleaning process completed. Cleaned data saved to 'cleaned_data.csv'.")
 

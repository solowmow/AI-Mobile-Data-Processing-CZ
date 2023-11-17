# data_normalization.py

import numpy as np

def min_max_normalization(data):
    """
    Perform min-max normalization on the input data.

    Parameters:
    - data: List or array containing the input data.

    Returns:
    - normalized_data: List or array with normalized values.
    """

    min_val = min(data)
    max_val = max(data)

    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]

    return normalized_data

def z_score_normalization(data):
    """
    Perform z-score normalization on the input data.

    Parameters:
    - data: List or array containing the input data.

    Returns:
    - normalized_data: List or array with normalized values.
    """

    mean = np.mean(data)
    std_dev = np.std(data)

    normalized_data = [(x - mean) / std_dev for x in data]

    return normalized_data

def decimal_scaling(data):
    """
    Perform decimal scaling normalization on the input data.

    Parameters:
    - data: List or array containing the input data.

    Returns:
    - normalized_data: List or array with normalized values.
    """

    max_val = max(data)
    num_digits = len(str(abs(max_val)))

    normalized_data = [x / (10 ** num_digits) for x in data]

    return normalized_data

# Example usage:
if __name__ == "__main__":
    # Example dataset (replace this with your own data)
    input_data = [2, 5, 10, 15, 7]

    # Perform different normalizations
    normalized_min_max = min_max_normalization(input_data)
    normalized_z_score = z_score_normalization(input_data)
    normalized_decimal_scaling = decimal_scaling(input_data)

    print("Original Data:", input_data)
    print("Min-Max Normalized Data:", normalized_min_max)
    print("Z-Score Normalized Data:", normalized_z_score)
    print("Decimal Scaling Normalized Data:", normalized_decimal_scaling)
 

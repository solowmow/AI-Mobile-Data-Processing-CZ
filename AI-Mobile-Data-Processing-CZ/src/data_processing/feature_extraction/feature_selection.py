# feature_selection.py

# Import necessary libraries
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression

def select_best_features(data, target_column, num_features=10):
    """
    Selects the top 'num_features' features using SelectKBest with f_regression scoring.

    Args:
    - data (DataFrame): The input data containing features and target.
    - target_column (str): The name of the column representing the target variable.
    - num_features (int): Number of top features to select (default: 10).

    Returns:
    - selected_features (list): List of names of selected features.
    """

    # Separate features and target variable
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Feature selection using SelectKBest
    selector = SelectKBest(score_func=f_regression, k=num_features)
    X_new = selector.fit_transform(X, y)

    # Get selected feature indices
    selected_feature_indices = selector.get_support(indices=True)

    # Get the names of selected features
    selected_features = list(X.columns[selected_feature_indices])

    return selected_features

# Example usage:
if __name__ == "__main__":
    # Load data (assuming 'data' is a DataFrame with features and target)
    # Replace this with your actual data loading process
    data = pd.read_csv('your_data.csv')

    # Target column name
    target_column_name = 'target'

    # Select top features
    selected_features = select_best_features(data, target_column_name)

    # Display selected features
    print("Selected Features:")
    print(selected_features)
 

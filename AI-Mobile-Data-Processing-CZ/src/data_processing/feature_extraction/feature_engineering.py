import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def handle_missing_values(df):
    # Handle missing values: Fill with mean or other strategies
    df.fillna(df.mean(), inplace=True)
    return df

def scale_numeric_features(df, numeric_columns):
    # Scale numerical features using StandardScaler
    scaler = StandardScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
    return df

def apply_pca(df, numeric_columns, n_components=3):
    # Apply PCA to numeric features
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(df[numeric_columns])
    
    # Create new PCA columns in the DataFrame
    for i in range(n_components):
        df[f'PCA_Component_{i+1}'] = pca_result[:, i]
    
    return df

def engineer_features(data_path):
    # Load the dataset
    data = pd.read_csv(data_path)
    
    # List of numeric columns for feature engineering
    numeric_columns = ['feature_1', 'feature_2', 'feature_3']
    
    # Handle missing values
    data = handle_missing_values(data)
    
    # Scale numeric features
    data = scale_numeric_features(data, numeric_columns)
    
    # Apply PCA to numeric features
    data = apply_pca(data, numeric_columns)
    
    return data

if __name__ == "__main__":
    # Path to the dataset file
    dataset_path = 'path/to/your/dataset.csv'
    
    # Perform feature engineering
    engineered_data = engineer_features(dataset_path)
    
    # Save the engineered data
    engineered_data.to_csv('path/to/save/engineered_data.csv', index=False)
 

import numpy as np
from sklearn.metrics.pairwise import euclidean_distances


def rkNN_imputation(dataset, target_column, knn_columns, k=5):
    """
    Perform Ranked K-Nearest Neighbors (RkNN) imputation on the given dataset.

    Parameters:
    - dataset: pandas DataFrame containing the data to be imputed
    - target_column: column name in which missing values should be imputed
    - knn_columns: list of column names to be used for calculating the distance between neighbors
    - k: number of nearest neighbors to consider for imputation

    Returns:
    - dataset: DataFrame with imputed values
    """
    # Select only rows with missing values in the target_column
    missing_rows = dataset[dataset[target_column].isnull()]

    # Calculate pairwise distances between all rows (Euclidean distance)
    distances = euclidean_distances(dataset[knn_columns], dataset[knn_columns])

    # Apply imputation using Ranked KNN
    for idx, row in missing_rows.iterrows():
        # Get distances for the missing row to all other rows
        row_distances = distances[idx]

        # Rank the rows based on the distances and get the indices of the nearest neighbors
        nearest_neighbors_idx = np.argsort(row_distances)[1:k + 1]  # Ignore the row itself (index 0)

        # Use the neighbors' values for imputation
        neighbors_values = dataset.iloc[nearest_neighbors_idx][target_column]

        # Impute the missing value as the average of the ranked nearest neighbors
        imputed_value = np.mean(neighbors_values)

        # Replace the missing value with the imputed value
        dataset.at[idx, target_column] = imputed_value

    return dataset

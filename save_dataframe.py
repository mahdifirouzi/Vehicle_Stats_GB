def save_dataframe(df, file_name, file_format='csv', save_index=False):
    """
    Save the DataFrame to a file in the specified format (CSV, Excel, JSON, Parquet, HDF5, Feather, Pickle).

    Parameters:
    - df: The DataFrame to save.
    - file_name: The name of the file (without extension).
    - file_format: The format to save as ('csv', 'excel', 'json', 'parquet', 'hdf5', 'feather', 'pickle'). Default is 'csv'.
    - save_index: Whether to save the DataFrame's index in the file (True or False). Default is False.

    Returns:
    - None
    """
    # Ensure the file format is valid
    if file_format == 'csv':
        # Save as CSV
        df.to_csv(f"{file_name}.csv", index=save_index)
        print(f"DataFrame saved as {file_name}.csv")

    elif file_format == 'excel':
        # Save as Excel
        df.to_excel(f"{file_name}.xlsx", index=save_index)
        print(f"DataFrame saved as {file_name}.xlsx")

    elif file_format == 'json':
        # Save as JSON
        df.to_json(f"{file_name}.json", orient='records', lines=True)
        print(f"DataFrame saved as {file_name}.json")

    elif file_format == 'parquet':
        # Save as Parquet
        df.to_parquet(f"{file_name}.parquet")
        print(f"DataFrame saved as {file_name}.parquet")

    elif file_format == 'hdf5':
        # Save as HDF5
        df.to_hdf(f"{file_name}.h5", key='df', mode='w')
        print(f"DataFrame saved as {file_name}.h5")

    elif file_format == 'feather':
        # Save as Feather
        df.to_feather(f"{file_name}.feather")
        print(f"DataFrame saved as {file_name}.feather")

    elif file_format == 'pickle':
        # Save as Pickle
        df.to_pickle(f"{file_name}.pkl")
        print(f"DataFrame saved as {file_name}.pkl")

    else:
        print("Invalid file format. Please choose 'csv', 'excel', 'json', 'parquet', 'hdf5', 'feather', or 'pickle'.")

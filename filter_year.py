def filter_by_year_quarter(df, year, quarter, new_column_name):
    # Create the year-quarter string (e.g., '2024Q2')
    year_quarter = f"{year}Q{quarter}"

    # Check if the column exists in the DataFrame
    if year_quarter in df.columns:
        # Select the first three columns and the desired year-quarter column
        filtered_df = df.iloc[:, :3].join(df[[year_quarter]], how='left')

        # Rename the year-quarter column to the new column name provided by the user
        filtered_df = filtered_df.rename(columns={year_quarter: new_column_name})
    else:
        print(f"Column {year_quarter} not found in the DataFrame.")
        filtered_df = pd.DataFrame()  # Return an empty DataFrame if column not found

    return filtered_df

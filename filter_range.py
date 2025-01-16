def filter_by_year_range(df, start_year, end_year, quarter):
    # Create a list of year-quarter strings (e.g., ['2024Q1', '2023Q1', ..., '2020Q1'])
    year_quarters = [f"{year}Q{quarter}" for year in range(start_year, end_year - 1, -1)]

    # Check if the year-quarter columns exist in the DataFrame
    if all(col in df.columns for col in year_quarters):
        # Select the first three columns and the year-quarter columns
        filtered_df = df.iloc[:, :3].join(df[year_quarters], how='left')

        # Rename the columns to keep only the year (e.g., '2024' instead of '2024Q1')
        renamed_columns = {year_quarter: str(year_quarter[:4]) for year_quarter in year_quarters}
        filtered_df = filtered_df.rename(columns=renamed_columns)
    else:
        print("One or more columns not found in the DataFrame.")
        filtered_df = pd.DataFrame()  # Return an empty DataFrame if any column is not found

    return filtered_df
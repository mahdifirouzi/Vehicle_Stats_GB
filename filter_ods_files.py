import pandas as pd
import re  # For cleaning year values

def filter_and_copy_sheets(sheet_to_file_map, ods_directory, output_file_prefix, year_filter):
    """
    Reads sheets from specified ODS files, filters data by the given year,
    adjusts year cell values, and saves the filtered data into separate Excel files.

    Parameters:
    - sheet_to_file_map: Dictionary mapping sheet names to ODS filenames.
    - ods_directory: Directory containing the ODS files.
    - output_file_prefix: Prefix for the output file.
    - year_filter: Year to filter data in the sheets.
    """
    # Define the output file name with the year appended
    output_excel = f"{output_file_prefix}_{year_filter}.xlsx"

    # Prepare the output Excel writer
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        for sheet_name, ods_filename in sheet_to_file_map.items():
            ods_filepath = f"{ods_directory}/{ods_filename}"

            try:
                # Read the sheet, specifying the header row
                sheet_data = pd.read_excel(ods_filepath, sheet_name=sheet_name, header=5, engine='odf')

                # Identify the "Year" column dynamically
                year_column = next((col for col in sheet_data.columns if "Year" in col), None)

                if year_column:
                    # Debug: Output year column values
                    print(f"Processing sheet: {sheet_name} | Year Column Detected: {year_column}")
                    print(f"Year Column Values: {sheet_data[year_column].dropna().unique()}")

                    # Clean year values to remove notes like "[r]" or expand ranges like "2006 to 2010"
                    def clean_year(value):
                        if isinstance(value, str):
                            # Handle ranges like "2006 to 2010"
                            if "to" in value:
                                start, end = map(int, re.findall(r"\d{4}", value))
                                return list(range(start, end + 1))
                            # Handle single years with notes like "2020 [r]"
                            match = re.match(r"(\d{4})", value)  # Extract year as a number
                            return int(match.group(1)) if match else None
                        return value

                    # Apply cleaning to the year column and expand ranges if necessary
                    sheet_data["Expanded_Year"] = sheet_data[year_column].apply(clean_year)

                    # Replace original year values with the cleaned ones
                    def replace_year(value):
                        if isinstance(value, list):  # Replace ranges with the first year
                            return value[0]
                        return value

                    sheet_data[year_column] = sheet_data["Expanded_Year"].apply(replace_year)

                    # Debug: Output cleaned year values
                    print(f"Cleaned Year Values in '{sheet_name}': {sheet_data[year_column].dropna().unique()}")

                    # Filter rows where the cleaned year matches year_filter
                    filtered_data = sheet_data[sheet_data["Expanded_Year"].apply(
                        lambda x: year_filter in x if isinstance(x, list) else x == year_filter)]

                    # Debug: Check if filtered data is empty
                    if filtered_data.empty:
                        print(f"No data for year {year_filter} in sheet '{sheet_name}' of file '{ods_filepath}'.")
                    else:
                        # Drop the temporary "Expanded_Year" column before writing
                        filtered_data = filtered_data.drop(columns=["Expanded_Year"])

                        # Write the filtered data to the output Excel file
                        filtered_data.to_excel(writer, sheet_name=sheet_name[:31], index=False)
                else:
                    print(f"Year column not found in sheet '{sheet_name}' of file '{ods_filepath}'.")

            except Exception as e:
                print(f"Error processing sheet '{sheet_name}' from file '{ods_filepath}': {e}")

    print(f"Processing complete. Filtered data saved to '{output_excel}'.")


# Dictionary mapping sheet names to ODS filenames
sheet_to_file_map = {
    "NTS0303a_trips": "nts0303.ods",
    "NTS0303c_miles": "nts0303.ods",
    "NTS0303d_trip_length": "nts0303.ods",
    "NTS0303e_time": "nts0303.ods",
    "NTS0303f_trip_duration": "nts0303.ods",
    "NTS0308a_trips": "nts0308.ods",
    "NTS0308b_trips_cumulative_%": "nts0308.ods",
    "NTS0308c_distance": "nts0308.ods",
    "NTS0308d_distance_cumulative_%": "nts0308.ods",
    "NTS0313": "nts0313.ods",
    "NTS0409a_trips": "nts0409.ods",
    "NTS0409b_distance": "nts0409.ods",
    "NTS0501": "nts0501.ods",
    "NTS0502a_start_time_by_purpose": "nts0502.ods",
    "NTS0502b_purpose_by_start_time": "nts0502.ods",
    "NTS0504a_day_mode": "nts0504.ods",
    "NTS0504b_day_purpose": "nts0504.ods",
    "NTS0504c_month_mode": "nts0504.ods",
    "NTS0504d_month_purpose": "nts0504.ods",
    "NTS0904": "nts0904.ods"
}

# Parameters
ods_directory = '.'  # Directory containing ODS files
output_file_prefix = 'NTS_Data_filtered'  # Prefix for the output file
# IT should be after 2020 before some data are mixec up before that
year_to_filter = 2023  # Year to filter the data

# Run the function
filter_and_copy_sheets(sheet_to_file_map, ods_directory, output_file_prefix, year_to_filter)

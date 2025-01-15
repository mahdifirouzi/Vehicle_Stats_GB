import pandas as pd
import os

# Load the CSV file into a DataFrame from the current directory
file_name = "df_VEH0120_GB.csv"
current_directory = os.getcwd()

# Construct the full file path
file_path = os.path.join(current_directory, file_name)

df_Vehicle_Stat_UK_ALL = pd.read_csv(file_path)

# Filter the dataframe for "Cars" in the 'BodyType' column
Car_Stat_UK_All = df_Vehicle_Stat_UK_ALL[df_Vehicle_Stat_UK_ALL['BodyType'] == 'Cars']

# Filter the dataframe for "Battery electric" in the 'Fuel' column
BECar_Stat_UK_All = Car_Stat_UK_All[Car_Stat_UK_All['Fuel'] == 'Battery electric']

# Filter the dataframe for "Licensed" in the 'LicenceStatus' column
BECar_Stat_UK_Registered = BECar_Stat_UK_All[BECar_Stat_UK_All['LicenceStatus'] == 'Licensed']


BECar_Stat_UK_Registered.head()  # Show the first few rows of the final dataframe for inspection
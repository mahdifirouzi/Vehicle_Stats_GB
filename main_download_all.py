# Import the function from the download_helper.py file
from vehicle_data_downloader import download_file_by_xpath

# This function will download the file corresponding to the key "df_VEH0120_GB" from the config.yml file.
# It fetches the XPath from the YAML file, locates the link on the webpage, and then downloads the related CSV file.

# Download the file for "df_VEH0120_GB" - Vehicles at the end of the quarter by licence status, body type, make, generic model, and model for Great Britain
download_file_by_xpath("config.yml", "df_VEH0120_GB")

# Download the file for "df_VEH0120_UK" - Vehicles at the end of the quarter by licence status, body type, make, generic model, and model for the United Kingdom
download_file_by_xpath("config.yml", "df_VEH0120_UK")

# Download the file for "df_VEH0160_GB" - Vehicles registered for the first time in Great Britain by licence status, body type, make, generic model, and model
download_file_by_xpath("config.yml", "df_VEH0160_GB")

# Download the file for "df_VEH0160_UK" - Vehicles registered for the first time in the United Kingdom by licence status, body type, make, generic model, and model
download_file_by_xpath("config.yml", "df_VEH0160_UK")

# Download the file for "df_VEH0124_AM" - Vehicles licensed in the United Kingdom with Make starting with A to M, by licence status, body type, make, generic model, and model
download_file_by_xpath("config.yml", "df_VEH0124_AM")

# Download the file for "df_VEH0124_NZ" - Vehicles licensed in the United Kingdom with Make starting with N to Z, by licence status, body type, make, generic model, and model
download_file_by_xpath("config.yml", "df_VEH0124_NZ")

# Download the file for "df_VEH0220" - Vehicles licensed in the United Kingdom by engine size and other details such as body type, make, and model
download_file_by_xpath("config.yml", "df_VEH0220")

# Download the file for "df_VEH0270" - Vehicles registered for the first time in the United Kingdom by engine size, body type, make, and model
download_file_by_xpath("config.yml", "df_VEH0270")

# Download the file for "df_VEH0125" - Vehicles licensed in the United Kingdom and Great Britain by small geography, including details such as LSOA11CD and LSOA11NM
download_file_by_xpath("config.yml", "df_VEH0125")

# Download the file for "df_VEH0135" - Licensed ultra low emission vehicles in the United Kingdom by small geography, including LSOA11CD and LSOA11NM
download_file_by_xpath("config.yml", "df_VEH0135")

# Download the file for "df_VEH0145" - Licensed plug-in vehicles in the United Kingdom by small geography, including LSOA11CD and LSOA11NM
download_file_by_xpath("config.yml", "df_VEH0145")

# Download the file for "df_VEH0520" - Licensed heavy goods vehicles and zero emission light goods vehicles in the United Kingdom, including details like tax class, wheel plan, fuel, and more
download_file_by_xpath("config.yml", "df_VEH0520")


import os
import requests
import zipfile
from io import BytesIO

# URL of the ZIP file
url = "https://assets.publishing.service.gov.uk/media/66cebb52face0992fa41f66a/nts-2023-ods-tables.zip"


# Function to download and extract the ZIP file
def download_and_extract_zip(url, folder_name="NTS_updated"):
    try:
        # Create the folder if it does not exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Download the ZIP file
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Extract the ZIP file
        with zipfile.ZipFile(BytesIO(response.content)) as z:
            z.extractall(folder_name)
        print("Files extracted successfully to:", folder_name)
    except requests.exceptions.RequestException as e:
        print("Error downloading the file:", e)
    except zipfile.BadZipFile:
        print("The downloaded file is not a valid ZIP file.")


# Call the function
download_and_extract_zip(url)

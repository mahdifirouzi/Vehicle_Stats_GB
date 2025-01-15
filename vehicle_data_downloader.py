import requests
import yaml
from lxml import html


def download_file_by_xpath(config_file, data_key):
    # Step 1: Read the XPath configuration from the YAML file
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    # Step 2: Get the XPath for the requested data key
    if data_key not in config:
        print(f"Error: '{data_key}' not found in configuration.")
        return

    xpath = config[data_key]

    # Step 3: Send a GET request to the page containing the data links
    url = "https://www.gov.uk/government/statistical-data-sets/vehicle-licensing-statistics-data-files"
    response = requests.get(url)

    # Step 4: Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the page content using lxml's HTML parser
        tree = html.fromstring(response.content)

        # Step 5: Extract the link for the requested data using the provided XPath
        link = tree.xpath(xpath + "/@href")

        if link:
            # Get the full URL of the CSV file
            csv_url = link[0]
            if not csv_url.startswith('http'):
                csv_url = 'https://www.gov.uk' + csv_url

            # Step 6: Download the file
            csv_response = requests.get(csv_url)

            if csv_response.status_code == 200:
                # Save the CSV file
                file_name = f"{data_key}.csv"
                with open(file_name, "wb") as file:
                    file.write(csv_response.content)
                print(f"File '{file_name}' downloaded successfully!")
            else:
                print(f"Failed to download the file. Status code: {csv_response.status_code}")
        else:
            print(f"Link for '{data_key}' not found using the provided XPath.")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")


# Example usage: call the function to download the df_VEH0120_GB file
#download_file_by_xpath("config.yml", "df_VEH0120_GB")

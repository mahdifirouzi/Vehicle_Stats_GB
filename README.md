# National Travel Statistics (NTS) Data Processor

This repository provides tools to download, extract, and process the UK's National Travel Statistics (NTS) data. It simplifies accessing and analyzing travel data for research, reporting, or decision-making.

---

## Features

- **Automated Data Retrieval**: 
  - Download the official NTS ZIP file directly from the UK Government's website.
  - Extract its contents to a specified folder.

- **Customizable Data Filtering**:
  - Filter data from ODS files based on specific years.
  - Clean and adjust year columns (e.g., handle ranges like "2006 to 2010").
  - Save filtered results to an Excel file.

---

## Repository Structure

```plaintext
.
├── download_extract.py     # Script to download and extract NTS data
├── filter_ods_files.py     # Script to filter and process extracted ODS files
├── LICENSE                 # License file for the repository
└── README.md               # Documentation for the repository

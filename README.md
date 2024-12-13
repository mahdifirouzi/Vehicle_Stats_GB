# National Travel Statistics (NTS) Data Processor

This repository provides tools to download, extract, and process the UK's National Travel Statistics (NTS) data. It simplifies accessing and analyzing travel data for research, reporting, or decision-making.

![Department for Transport Logo](https://via.placeholder.com/150?text=Department+for+Transport+Logo)  
![Nottingham Trent University Logo](https://via.placeholder.com/150?text=NTU+Logo)

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

## Prerequisites

### Software Requirements
- **Python**: 3.7 or higher
- **Required Libraries**: `pandas`, `requests`, `openpyxl`, `odfpy`

### Installing Dependencies
Use the following command to install all required libraries:

```bash
pip install pandas requests openpyxl odfpy
```

---

## Usage

### 1. Download and Extract Data
Run `download_extract.py` to download the NTS ZIP file and extract its contents into a folder named `NTS_updated` in the current directory.

```bash
python download_extract.py
```

### 2. Filter and Process ODS Files
Run `filter_ods_files.py` to filter ODS files by year and save the processed data to an Excel file.

```bash
python filter_ods_files.py
```

#### Customize Parameters
Modify the script to set:
- `sheet_to_file_map`: Maps sheet names to ODS filenames.
- `ods_directory`: Path to the directory containing ODS files.
- `output_file_prefix`: Prefix for the output Excel file.
- `year_to_filter`: Year to filter the data (e.g., `2023`).

---

## Example Workflow

1. Clone this repository:

```bash
git clone https://github.com/yourusername/NTS-Data-Processor.git
cd NTS-Data-Processor
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the scripts in sequence:
   - First, download and extract the data:

     ```bash
     python download_extract.py
     ```

   - Then, filter the data:

     ```bash
     python filter_ods_files.py
     ```

4. Find the filtered Excel file in the same directory (e.g., `NTS_Data_filtered_2023.xlsx`).

---

## Contribution Guidelines

We welcome contributions to improve this repository. If you'd like to contribute, please fork the repository, make your changes, and create a pull request.

---

## License

This repository is licensed under the Creative Commons Attribution License (CC BY 4.0). See `LICENSE` for details.

### Related Publication
[Firouzi, M., Nazar, M. S., Shafie-khah, M., & Catalão, J. P. S. (2023). Integrated framework for modeling the interactions of plug-in hybrid electric vehicles aggregators, parking lots and distributed generation facilities in electricity markets. *Applied Energy, 334*, 120703.](https://doi.org/10.1016/j.apenergy.2023.120703)

---

## Acknowledgments

- **Data Source**: UK Government's National Travel Statistics.

- **Organization**: Nottingham Trent University (Gridlab)  




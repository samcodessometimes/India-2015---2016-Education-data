Here's the README document revised for UK English:

---

# Indian School Education Data Analysis

This repository contains Python scripts for analysing Indian school education data from the 2015-16 academic year. The analysis focuses on district-wise and state-wise educational data, including metrics related to schools and teachers.

## Contents

- **Data Files**
  - `2015_16_Districtwise.csv` - District-level data for schools and teachers.
  - `2015_16_Statewise_Elementary.csv` - State-level data for elementary schools.
  - `2015_16_Statewise_Secondary.csv` - State-level data for secondary schools.

- **Scripts**
  - `data_analysis.py` - Python script for cleaning, summarising, and analysing the data.

## Getting Started

### Prerequisites

- Python 3.x
- Pandas library

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/India-2015-2016-Education-data.git
   cd repository-name
   ```

2. Install the required Python packages:
   ```bash
   pip install pandas
   ```

### Usage

1. Ensure that the data files (`2015_16_Districtwise.csv`, `2015_16_Statewise_Elementary.csv`, `2015_16_Statewise_Secondary.csv`) are placed in the `Education data` directory within the repository.

2. Run the Python script to perform data cleaning, summarising, and analysis:
   ```bash
   python data_analysis.py
   ```

### Script Overview

- **Data Import**: Loads CSV files into Pandas DataFrames.
- **Missing Values**: Identifies and removes rows with missing values.
- **Descriptive Statistics**: Provides summary statistics for each dataset.
- **Data Analysis Functions**:
  - `calculate_average()`: Computes the average number of schools in rural areas with only primary schools.
  - `calculate_teacher_totals()`: Summarises total numbers of teachers by category.
  - `calculate_school_totals()`: Computes totals for various types of schools.
- **Data Aggregation**: Aggregates data at the district and state levels.
- **Percentage Calculations**: Computes percentages of government and private schools.
- **Data Saving**: Saves cleaned and summarised data into new CSV files.

### Results

- Cleaned datasets are saved as:
  - `cleaned_districtwise_data.csv`
  - `cleaned_statewise_elementary_data.csv`
  - `cleaned_statewise_secondary_data.csv`
- These files are located in the `Education data` directory.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

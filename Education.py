
#This dataset contains district and state wise Indian primary and secondary school education data for 2015-16- compromised of Districitwise and State.

# Import pandas library to import data

import pandas as pd

# Import data using full file path with files located in the "Education data" folder.


df_districtwise = pd.read_csv('/Users/tiangaysamandia/Documents/Education data/2015_16_Districtwise.csv')
df_statewise_elementary = pd.read_csv('/Users/tiangaysamandia/Documents/Education data/2015_16_Statewise_Elementary.csv')
df_statewise_secondary = pd.read_csv('/Users/tiangaysamandia/Documents/Education data/2015_16_Statewise_Secondary.csv')

# Display the first few rows of each dataset to understand the structure

print("Districtwise Data:")
print(df_districtwise.head())
print("\nStatewise Elementary Data:")
print(df_statewise_elementary.head())

# Check for missing values in each dataset

print("\nMissing Values in Districtwise Data:")
print(df_districtwise.isnull().sum())
print("\nMissing Values in Statewise Elementary Data:")
print(df_statewise_elementary.isnull().sum())
print("\nMissing Values in Statewise Secondary Data:")
print(df_statewise_secondary.isnull().sum())

 # Remove rows with missing data
df_districtwise_clean = df_districtwise.dropna()
df_statewise_elementary_clean = df_statewise_elementary.dropna()
df_statewise_secondary_clean = df_statewise_secondary.dropna()


# column names
print(df_districtwise_clean.columns)


#Data Analysis
   # Descriptive Statistics- Summary of the numerical data in each DataFrame

print("Districtwise Data Statistics:")
print(df_districtwise.describe())

print("\nStatewise Elementary Data Statistics:")
print(df_statewise_elementary.describe())

print("\nStatewise Secondary Data Statistics:")
print(df_statewise_secondary.describe())


for column in df_districtwise.columns:
    print(f"Column: {column}")
    print(df_districtwise[column].unique())
    print("\n")

# Calculate the average number of number of Schools in the District that are in Rural areas with only Primary School - No Upper Primary


def calculate_average(csv_file, column_name):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        
        # Check if the column exists
        if column_name in df.columns:
            # Calculate the mean of the specified column
            average_value = df[column_name].mean()
            return average_value
        else:
            raise ValueError(f"Column '{column_name}' does not exist in the CSV file.")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{csv_file}' was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

# Example usage
csv_file = '/Users/tiangaysamandia/Documents/Education data/2015_16_Districtwise.csv'  # Path to the CSV file
column_name = 'SCH1GR'  # Column to calculate the average for number of rural schools with onyl primary school, no upper primary school.

try:
    average = calculate_average(csv_file, column_name)
    if pd.isna(average):
        print(f"The column '{column_name}' contains no valid numeric data.")
    else:
        print(f"The average value in the '{column_name}' column is {average:.2f}")
except ValueError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except RuntimeError as e:
    print(e)


# Checking column names in District wise data# Checking column names in District wise data



    # Path to your CSV file
csv_file = '/Users/tiangaysamandia/Documents/Education data/2015_16_Districtwise.csv'

try:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Print the column names
    print("Column names in the CSV file:")
    print(df.columns.tolist())
    
except FileNotFoundError:
    print(f"The file '{csv_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


#Teachers column names: 'TCH1G', 'TCH2G', 'TCH3G', 'TCH4G', 'TCH5G', 'TCH6G', 'TCH7G', 'TCH9G', 'TCHTOTG', 'TCH1P', 'TCH2P', 'TCH3P', 'TCH4P', 'TCH5P', 'TCH6P', 'TCH7P', 'TCH9P', 'TCHTOTP',
    # 'TCH1M', 'TCH2M', 'TCH3M', 'TCH4M', 'TCH5M', 'TCH6M', 'TCH7M', 'TCH9M', 'TCHTOTM

# Column: Total number of teachers: 'TCHTOTG', 'TCHTOTP', 'TCHTOTM'

# Total number of Teachers in the District# Total number of Teachers in the District


def calculate_teacher_totals(csv_file, columns):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        
        # Check if all specified columns exist
        for column in columns:
            if column not in df.columns:
                raise ValueError(f"Column '{column}' does not exist in the CSV file.")
        
        # Calculate totals for each category
        total_government = df['TCHTOTG'].sum()
        total_private = df['TCHTOTP'].sum()
        total_unrecognised = df['TCHTOTM'].sum()
        
        # Calculate the overall total number of teachers
        total_teachers = total_government + total_private + total_unrecognised
        
        return total_government, total_private, total_unrecognised, total_teachers
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{csv_file}' was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

# File path to the district-wise CSV file
csv_file = '/Users/tiangaysamandia/Documents/Education data/2015_16_Districtwise.csv'

# List of column names containing the number of teachers
columns = [
    'TCHTOTG',  # Government
    'TCHTOTP',  # Private
    'TCHTOTM'   # Unrecognised
]

try:
    total_government, total_private, total_unrecognised, total_teachers = calculate_teacher_totals(csv_file, columns)
    print(f"Total number of government teachers: {total_government:.0f}")
    print(f"Total number of private teachers: {total_private:.0f}")
    print(f"Total number of unrecognised teachers: {total_unrecognised:.0f}")
    print(f"Total number of teachers in the district: {total_teachers:.0f}")
except ValueError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except RuntimeError as e:
    print(e)

# Column names for number of schools in the district, total number of students in the district, total number of schools in the state

  #Number of schools in the district


def calculate_school_totals(csv_file):
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        
        # List of column names for which totals need to be calculated
        columns = {
            'SCHTOTG': 'Government schools total',
            'SCHTOTP': 'Private schools total',
            'SCHTOTM': 'Unrecognised schools total',
            'SCHTOTGR': 'Government rural schools total',
            'SCHTOTGA': 'Government & aiders total',
            'SCHTOTPR': 'Private schools rural total'
        }
        
        # Check if all specified columns exist
        for column in columns:
            if column not in df.columns:
                raise ValueError(f"Column '{column}' does not exist in the CSV file.")
        
        # Calculate totals for each type of school
        total_government = df['SCHTOTG'].sum()
        total_private = df['SCHTOTP'].sum()
        total_unrecognised = df['SCHTOTM'].sum()
        total_government_rural = df['SCHTOTGR'].sum()
        total_government_aiders = df['SCHTOTGA'].sum()
        total_private_rural = df['SCHTOTPR'].sum()
        
        # Calculate the overall total number of schools
        total_schools = total_government + total_private + total_unrecognised + total_government_rural + total_government_aiders + total_private_rural
        
        # Return the results
        return {
            'Total Government Schools': total_government,
            'Total Private Schools': total_private,
            'Total Unrecognised Schools': total_unrecognised,
            'Total Government Rural Schools': total_government_rural,
            'Total Government & Aiders': total_government_aiders,
            'Total Private Rural Schools': total_private_rural,
            'Overall Total Schools': total_schools
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{csv_file}' was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

# Path to the district-wise CSV file
csv_file = '/Users/tiangaysamandia/Documents/Education data/2015_16_Districtwise.csv'

# Calculate and print the total  number of schools in the District
try:
    results = calculate_school_totals(csv_file)
    for key, value in results.items():
        print(f"{key}: {value:.0f}")
except ValueError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
except RuntimeError as e:
    print(e)

# Caculate the total number of states


# File paths
elementary_file_path = '/Users/tiangaysamandia/Documents/Education data/2015_16_Statewise_Elementary.csv'
secondary_file_path = '/Users/tiangaysamandia/Documents/Education data/2015_16_Statewise_Secondary.csv'

# Columns for state names
elementary_column = 'STATNAME'
secondary_column = 'statname'

# Load the data
elementary_data = pd.read_csv(elementary_file_path)
secondary_data = pd.read_csv(secondary_file_path)

# Get unique states from both datasets
elementary_states = set(elementary_data[elementary_column].unique())
secondary_states = set(secondary_data[secondary_column].unique())

# Calculate the total number of unique states between both datasets
total_unique_states = len(elementary_states.union(secondary_states))

# Print the result
print(f"Total number of unique states between both datasets: {total_unique_states}")


# Group by 'DISTNAME' (district name) and aggregate the sum of schools and teachers
district_summary = df_districtwise_clean.groupby('DISTNAME').agg({
    'SCHTOTG': 'sum',
    'SCHTOTP': 'sum',
    'SCHTOTM': 'sum',
    'TCHTOTG': 'sum',
    'TCHTOTP': 'sum',
    'TCHTOTM': 'sum'
}).reset_index()

# Display the summarized data
print("District-wise Summary:")
print(district_summary)

# Summarising at the state level
state_summary = df_districtwise_clean.groupby('STATNAME').agg({
    'SCHTOTG': 'sum',
    'SCHTOTP': 'sum',
    'SCHTOTM': 'sum',
    'TCHTOTG': 'sum',
    'TCHTOTP': 'sum',
    'TCHTOTM': 'sum'
}).reset_index()

print("State-wise Summary:")
print(state_summary)

#Calculate percentage of schools at District level
# Ensure that df_districtwise_clean is a copy of the original DataFrame
df_districtwise_clean = df_districtwise_clean.copy()

# Calculate the percentage of government and private schools in each district
df_districtwise_clean.loc[:, 'Government_School_Percentage'] = (
    df_districtwise_clean['SCHTOTG'] / df_districtwise_clean['SCHTOTG'].sum()
) * 100

df_districtwise_clean.loc[:, 'Private_School_Percentage'] = (
    df_districtwise_clean['SCHTOTP'] / df_districtwise_clean['SCHTOTP'].sum()
) * 100

# Print the updated DataFrame to see the new columns
print("District level School Percentages:")
print(df_districtwise_clean[['DISTNAME', 'Government_School_Percentage', 'Private_School_Percentage']].head())



# Calculate the total number of schools in each state for elementary data
state_summary_elementary = df_statewise_elementary.groupby('STATNAME').agg({
    'TCHTOTG': 'sum',  # Government schools
    'TCHTOTP': 'sum',  # Private schools
    'TCHTOTM': 'sum'   # Unrecognized schools
}).reset_index()

# Calculate the total number of schools in each state for secondary data
state_summary_secondary = df_statewise_secondary.groupby('statname').agg({
    'sch_1': 'sum',
    'sch_2': 'sum',
    'sch_3': 'sum',
    'sch_4': 'sum',
    'sch_5': 'sum',
    'sch_6': 'sum',
    'sch_7': 'sum',
    'sch_r_1': 'sum',
    'sch_r_2': 'sum',
    'sch_r_3': 'sum',
    'sch_r_4': 'sum',
    'sch_r_5': 'sum',
    'sch_r_6': 'sum',
    'sch_r_7': 'sum',
    'sch_u_1': 'sum',
    'sch_u_2': 'sum',
    'sch_u_3': 'sum',
    'sch_u_4': 'sum',
    'sch_u_5': 'sum',
    'sch_u_6': 'sum',
    'sch_u_7': 'sum'
}).reset_index()

# Combine the summaries from elementary and secondary into one DataFrame
state_summary = state_summary_elementary.merge(
    state_summary_secondary, left_on='STATNAME', right_on='statname', suffixes=('_elementary', '_secondary')
)

# Calculate the total number of schools by summing all relevant columns
state_summary['Total_SCHTOTG'] = state_summary['TCHTOTG'] + state_summary[['sch_1', 'sch_2', 'sch_3', 'sch_4', 'sch_5', 'sch_6', 'sch_7']].sum(axis=1)
state_summary['Total_SCHTOTP'] = state_summary['TCHTOTP'] + state_summary[['sch_1', 'sch_2', 'sch_3', 'sch_4', 'sch_5', 'sch_6', 'sch_7']].sum(axis=1)
state_summary['Total_SCHTOTM'] = state_summary['TCHTOTM'] + state_summary[['sch_1', 'sch_2', 'sch_3', 'sch_4', 'sch_5', 'sch_6', 'sch_7']].sum(axis=1)

# Calculate the total number of schools for rural and urban
total_rural_schools = state_summary[['sch_r_1', 'sch_r_2', 'sch_r_3', 'sch_r_4', 'sch_r_5', 'sch_r_6', 'sch_r_7']].sum(axis=1)
total_urban_schools = state_summary[['sch_u_1', 'sch_u_2', 'sch_u_3', 'sch_u_4', 'sch_u_5', 'sch_u_6', 'sch_u_7']].sum(axis=1)

# Calculate the total number of schools
total_schools = state_summary['Total_SCHTOTG'] + state_summary['Total_SCHTOTP'] + state_summary['Total_SCHTOTM']

# Calculate the percentage of each type of school within each state
state_summary['Government_School_Percentage_State'] = state_summary.apply(
    lambda row: (row['Total_SCHTOTG'] / total_schools[row.name]) * 100 if total_schools[row.name] > 0 else 0, axis=1
)
state_summary['Private_School_Percentage_State'] = state_summary.apply(
    lambda row: (row['Total_SCHTOTP'] / total_schools[row.name]) * 100 if total_schools[row.name] > 0 else 0, axis=1
)
state_summary['Unrecognized_School_Percentage_State'] = state_summary.apply(
    lambda row: (row['Total_SCHTOTM'] / total_schools[row.name]) * 100 if total_schools[row.name] > 0 else 0, axis=1
)

# Print the state-level summary with in-state school percentages
print("State-level Summary with In-State School Percentages:")
print(state_summary[['STATNAME', 'Government_School_Percentage_State', 'Private_School_Percentage_State', 'Unrecognized_School_Percentage_State']].head())

# Save the cleaned district-wise data
df_districtwise_clean.to_csv('/Users/tiangaysamandia/Documents/Education data/cleaned_districtwise_data.csv', index=False)

# Save the cleaned state-wise elementary data
df_statewise_elementary_clean.to_csv('/Users/tiangaysamandia/Documents/Education data/cleaned_statewise_elementary_data.csv', index=False)

# Save the cleaned state-wise secondary data
df_statewise_secondary_clean.to_csv('/Users/tiangaysamandia/Documents/Education data/cleaned_statewise_secondary_data.csv', index=False)

import pandas as pd

# Load the cleaned data
df_districtwise_clean = pd.read_csv('/Users/tiangaysamandia/Documents/Education data/cleaned_districtwise_data.csv')

# Rename columns
df_districtwise_clean.rename(columns={
    'DISTNAME': 'District',
    'STATNAME': 'State name',
    'STATCD' : 'State code',
    'DISTRICTS' : 'Number of Districts'
    # Add more columns as needed
}, inplace=True)

# Save the cleaned data with renamed columns
df_districtwise_clean.to_csv('/Users/tiangaysamandia/Documents/Education data/cleaned_districtwise_data.csv', index=False)

# For statewise elementary data
df_statewise_elementary_clean = pd.read_csv('/Users/tiangaysamandia/Documents/Education data/cleaned_statewise_elementary_data.csv')
df_statewise_elementary_clean.rename(columns={
    'DISTNAME': 'District',
    'STATNAME': 'State name',
    'STATCD' : 'State code',
    'DISTRICTS' : 'Number of Districts'
    # Add more columns as needed
}, inplace=True)

#Save the cleaned data with renamed columns
df_statewise_elementary_clean.to_csv('/Users/tiangaysamandia/Documents/Education data/cleaned_statewise_elementary_data.csv', index=False)

# For statewise secondary data
df_statewise_secondary_clean = pd.read_csv('/Users/tiangaysamandia/Documents/Education data/cleaned_statewise_secondary_data.csv')
df_statewise_secondary_clean.rename(columns={
    'statname': 'State',
    'distcd': 'Districts'
    # Add more columns as needed
}, inplace=True)
df_statewise_secondary_clean.to_csv('/Users/tiangaysamandia/Documents/Education data/cleaned_statewise_secondary_data.csv', index=False)

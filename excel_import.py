# excel_import.py
#
# functions to import data from excel file
import os
import pandas as pd
# functions
# Usage
DEFAULT_PATH = "/excel/default_template.xlsx"
test_path = "/excel/test_template.xlsx"

def get_excel_file_path(default_path: str) -> str:
    print(f"The default path for the Excel file is: {default_path}")
    use_default = input("Would you like to use the default path? (yes/no): ").strip().lower()

    if use_default == 'yes':
        return default_path
    else:
        file_path = input("Please enter the new path to your Excel file: ").strip()
        return file_path
user_provided_file_path = get_excel_file_path(DEFAULT_PATH)

def load_excel_file() -> dict:
    file_path = input("Please enter the path to your Excel file: ").strip()
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        print("The file does not exist. Please check the path and try again.")
        return {}
    
    try:
        # Load the Excel file
        data = pd.read_excel(file_path)
        
        # Validate the structure of the Excel file
        if not validate_excel_structure(data):
            print("The structure of the Excel file does not match the expected format.")
            return {}
        
        # Extract information
        extracted_entity_data = get_entity_data(data)
        
        return extracted_entity_data
        
    except Exception as e:
        print(f"An error occurred while loading the Excel file: {e}")
        return {}

def validate_excel_structure(dataframe: pd.DataFrame) -> bool:
    # Implement validation logic to check if all required columns exist
    required_columns = ['Column1', 'Column2', 'Column3']  # Replace with your actual column names
    return all(column in dataframe.columns for column in required_columns)

def get_entity_data(df, entity_name):
    """
    Get data for a specific entity from the DataFrame.
    """
    entity_data = df[df['Entity Name'] == entity_name].iloc[0]
    target = entity_data['Target']
    ct_order_number = entity_data['CT Order Number']
    domestic_state = entity_data['Domestic State']
    current_registered_agent = entity_data['Current Registered Agent']
    current_status = entity_data['Current Status']
    registration_date = entity_data['Registration Date']
    filing_type = entity_data['Filing Type']

    return {
        'Target': target,
        'CT Order Number': ct_order_number,
        'Domestic State': domestic_state,
        'Current Registered Agent': current_registered_agent,
        'Current Status': current_status,
        'Registration Date': registration_date,
        'Filing Type': filing_type
    }


# You can call load_excel_file() where appropriate in your questionnaire flow
def load_excel_data(file_path: str):
    try:
        # Load the Excel file
        df = pd.read_excel(file_path)

        # Validate the structure of the Excel file
        expected_columns = ['EntityName', 'FilingType', 'State']
        if not all(column in df.columns for column in expected_columns):
            raise ValueError("Excel file is missing one or more required columns.")

        # Perform additional validations...
        # For example, check if 'State' column has valid state abbreviations

        # If all validations pass, return the DataFrame
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error or re-raise it
        raise

# Usage
run_excel_test = load_excel_data(test_path)


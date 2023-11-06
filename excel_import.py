# excel_import.py
# functions to import data from excel file
import os
import pandas as pd

# Global constants and variables

test_path = "./excel/test_audit.xls"

# Function definitions
def get_excel_file_path(default_path: str) -> str:
    print(f"The default path for the Excel file is: {default_path}")
    use_default = input("Would you like to use the default path, custom input, or the test path? (yes/no/test): ").strip().lower()
    if use_default == 'test': 
        return test_path
    if use_default == 'yes':
        return default_path
    else:
        file_path = input("Please enter the new path to your Excel file: ").strip()
        return file_path

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

def load_excel_data(file_path: str):
    try:
        # Load the Excel file
        df = pd.read_excel(file_path)

        # Filter for DE filings
        df = df[df['Domestic Jurisdiction'] == 'DE']

        # Validate the structure of the Excel file
        expected_columns = ['Entity Name', 'Domestic Jurisdiction', 'Jurisdiction Audited']
        if not all(column in df.columns for column in expected_columns):
            raise ValueError("Excel file is missing one or more required columns for DE filings.")

        # Select only the relevant columns
        df = df[['Entity Name', 'Domestic Jurisdiction', 'Jurisdiction Audited']]

        # Rename columns to match expected keys in the rest of the application
        df.columns = ['EntityName', 'DomesticState', 'FilingState']

        # Return the filtered and processed DataFrame
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def validate_excel_structure(dataframe: pd.DataFrame) -> bool:
    # Implement validation logic to check if all required columns exist
    required_columns = ['Column1', 'Column2', 'Column3']  # Replace with your actual column names
    return all(column in dataframe.columns for column in required_columns)

def get_entity_data(df, entity_name):
    """
    Get data for a specific entity from the DataFrame.
    """
    entity_data = df[df['Entity Name'] == entity_name].iloc[0]
    #target = entity_data['Target']
    #ct_order_number = entity_data['CT Order Number']
    domestic_state = entity_data['Domestic State']
    current_registered_agent = entity_data['Current Registered Agent']
    registration_date = entity_data['Registration Date']

    return {
        'Entity Name': entity_name,
        'Domestic State': domestic_state,
        'Current Registered Agent': current_registered_agent,
        'Registration Date': registration_date,
    }
def review_and_confirm_data(df): ## DALIA HELP - IS THIS THE RIGHT WAY TO DO THIS?
    # df is a pandas DataFrame containing the loaded Excel data.
    # Iterate confirmation qury for each row in the DataFrame
    for index, row in df.iterrows():
        print(f"\nReviewing record {index + 1}/{len(df)}:")
        print(row)  # This prints the entire row for the user to review.
        confirmation = input("Is this information correct? (yes/no): ").strip().lower()
        if confirmation != 'yes':
            print("Please correct the data...")
            # Implement data correction logic here
        else:
            print("Data confirmed.")

# if __name__ == "__main__":
#    print("this is the test run of excel import.py")
#    user_provided_file_path = get_excel_file_path(DEFAULT_PATH)
#    run_excel_test = load_excel_data(user_provided_file_path)
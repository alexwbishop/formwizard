# main.py
#
# Import necessary modules and functions
from questionnaire.questionnaire import initiate_filing_questionnaire
from questionnaire.questionnaire import get_data
from questionnaire.questionnaire import domestic_state
from excel_import import get_excel_file_path, load_excel_data
from constants.config import DEFAULT_PATH
from enums.residency import determine_filing_nature

# function to ask user for data input method
def get_data_source_choice():
    # Prompt user for data import method, define it as a variable named choice
    choice = input("Would you like to import data from an Excel sheet (type 'excel') or input manually (type 'manual')? ")
    while choice not in ['excel', 'manual']:
        print("Invalid choice. Please choose 'excel' or 'manual'.")
        choice = input("Would you like to import data from an Excel sheet or input manually? ")
    # Send their choice to the main function
    return choice
# Define the main function that runs the program
def main():
    # Bootup message
    print("Welcome to FormWizard!")
    # Get the choice once at the beginning
    choice = get_data_source_choice() 
    # # If the user chooses to import from Excel, 
    if choice == 'excel':
        # handle the Excel file import and processing
        excel_file_path = get_excel_file_path(DEFAULT_PATH)
        # Load the Excel file and extract the data
        entity_data = load_excel_data(excel_file_path)
        # ... further processing of entity_data - ?
    # or if  the user chooses to input manually,
    elif choice == 'manual':
        # Start the questionnaire and ask how many filings are needed
        num_forms = initiate_filing_questionnaire() 
        for _ in range(num_forms):
            entity_data = get_data()
            # Determine residency class for each entry
            #domestic_state = entity_data['Domestic State'] - REDUNDANT - used on 
            # Use the correct function name and pass the required parameters
            entity_data['Residency'] = determine_filing_nature(domestic_state)
            # Further processing with entity_data such as validation, etc.
            #

# Ensure that the script only runs when it is not imported as a module
if __name__ == "__main__":
    main()
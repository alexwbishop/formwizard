# main.py
#
# Import necessary modules and functions
from questionnaire.questionnaire import initiate_filing_questionnaire
from questionnaire.questionnaire import get_data
from excel_import import get_excel_file_path, load_excel_data
from constants.config import DEFAULT_PATH
from residency import determine_filing_nature  # Import the function from residency.py

# Define the main function that runs the program
def main():
    print("Welcome to FormWizard!")
    # Get the choice once at the beginning
    choice = get_data_source_choice() 

    if choice == 'excel':
        # If the user chooses to import from Excel, handle the Excel file import and processing
        excel_file_path = get_excel_file_path(DEFAULT_PATH)
        entity_data = load_excel_data(excel_file_path)
        # ... further processing of entity_data
        # ...

    elif choice == 'manual':
        # Start the questionnaire and ask how many filings are needed
        num_forms = initiate_filing_questionnaire() 
        for _ in range(num_forms):
            entity_data = get_data()
            # Determine residency class for each entry
            domestic_state = entity_data['Domestic State']
            # Use the correct function name and pass the required parameters
            entity_data['Residency Class'] = determine_filing_nature(domestic_state)
            # Further processing with entity_data such as validation, etc.
            #

# Ensure that the script only runs when it is not imported as a module
if __name__ == "__main__":
    main()


'''# main.py
#
# Import necessary modules and functions
from questionnaire.questionnaire import initiate_filing_questionnaire
from questionnaire.questionnaire import get_data_source_choice
from excel_import import get_excel_file_path, load_excel_data
from questionnaire.questionnaire import get_data
from constants.config import DEFAULT_PATH
from residency import determine_filing_nature  # Import the function from residency.py

# Define the main function that runs the program
def main():
    print("Welcome to FormWizard!")
    # Get the choice once at the beginning
    choice = get_data_source_choice() 

    if choice == 'excel':
        # If the user chooses to import from Excel, handle the Excel file import and processing
        entity_data = get_data(choice)
        # ... further processing of entity_data
        # ...

    elif choice == 'manual':
        # Start the questionnaire and ask how many filings are needed
        num_forms = initiate_filing_questionnaire() 
        for _ in range(num_forms):
            entity_data = get_data(choice)
            # Determine residency class for each entry
            domestic_state = entity_data['Domestic State']
            # Use the correct function name and pass the required parameters
            entity_data['Residency Class'] = determine_filing_nature(domestic_state)
            # Further processing with entity_data such as validation, etc.
            #

# Ensure that the script only runs when it is not imported as a module
if __name__ == "__main__":
    main()'''
# main.py
#
##Here's a breakdown of the basic sequence:
#1. Imports: Various utility functions and classes are imported.
#2. The config, constants, and enums are loaded and set
#3. Main Function: An empty main() function is defined.
#4. Jurisdiction Questioning: Depending on the jurisdiction (CA or DE), the appropriate set of questions is triggered.
#5. Logging: A message logging function is called.
#6. Confirmation and Validation: Various functions are called to confirm and validate the user's input.
#7. Form Population: The form is populated based on the user's input.
#8. PDF Manipulation: Functions are called to manipulate the PDFs, such as merging them.
#9. Session Initialization: A session ID is generated, and various session-related attributes are set.
#10. Data Collection and Validation: A series of questions are asked to collect and validate the data for the form.
#11. Document Preparation: The form is prepared based on the collected data.
#
#1. Import necessary modules and functions
from questionnaire import initiate_filing_questionnaire
from questionnaire import get_data
from excel_import import get_excel_file_path, load_excel_data
from constants.config import DEFAULT_PATH
from enums.residency import determine_residency

# Function to ask the user to choose the data input method (Excel or Manual)
def get_data_source_choice():
    # Prompt user for data import method, store the response in 'choice'
    choice = input("Would you like to import data from an Excel sheet (type 'excel') or input manually (type 'manual')? ")
    # Loop to ensure a valid response is entered
    while choice not in ['excel', 'manual']:
        print("Invalid choice. Please choose 'excel' or 'manual'.")
        choice = input("Would you like to import data from an Excel sheet or input manually? ")
    # Return the user's choice to the calling function
    return choice

# Main function that orchestrates the form handling based on user input
def main(): 
    print("......warming up......") # FIRST MESSAGE #
    # Display a welcome message
    print("Welcome to FormWizard!") 
    # Prompt user for data source preference at the start
    print("We will now ask how you would like to input your data.")
    choice = get_data_source_choice() 
    # If the user opts for Excel import
    if choice == 'excel':
        print("You have chosen to import data from an Excel sheet. Please have your file path name ready to enter.")
        # Retrieve the path to the Excel file based on a default or user-provided path
        excel_file_path = get_excel_file_path(DEFAULT_PATH)
        # Load the data from the Excel file into 'entity_data'
        print("Loading data from Excel file...")
        entity_data = load_excel_data(excel_file_path)
        print("Data loaded. Validating...")
        # Send data to LOG FILE with import & Validation details?
        #entity_data = validate_entity_data(entity_data) 
        # Need to set up validate_entity_data function to check for completeness and correctness of the data.
        if not entity_data:  # If validation fails, handle it appropriately
            # Handle invalid data
            print("Invalid data found in Excel. Please correct the data and try again.")

        # Additional processing of the data from the Excel file can occur here

    # If the user decides on manual data input
    elif choice == 'manual':
        print("You have chosen to input data manually.")
        # Launch the questionnaire to determine the number of forms to process
        print("Booting up filing questionnaire. Please wait...")
        num_forms = initiate_filing_questionnaire() 
        # Loop to process each form as per the number specified
        for _ in range(num_forms):
            # Gather data manually for each form
            entity_data = get_data()
# DALIA HELP - Can the below be replaced with a call to determine_residency function in questionnaire.py?
            # Determine and assign residency status based on the domestic state provided
            print("Determining residency based on data provided...")
            domestic_state = entity_data['Domestic State']
            entity_data['Residency'] = determine_residency(domestic_state)
            print("Residency determined successfully: " + entity_data['Residency'])
            # Additional steps to process each manually entered 'entity_data' can be done here

# Entry point check to prevent code from executing when imported
if __name__ == "__main__":
    main()

# main.py
#
# Import necessary modules and functions
from questionnaire.questionnaire import initiate_filing_questionnaire
from questionnaire.questionnaire import get_data_source_choice
from excel_import import get_excel_file_path, load_excel_data
from questionnaire.questionnaire import get_data
from constants.config import DEFAULT_PATH  # 

# Define the main function that runs the program
def main():
    print("Welcome to FormWizard!")
    choice = input("Would you like to import data from an Excel sheet (type 'excel') or input manually (type 'manual')? ")
    data = get_data(choice)  # Now you pass the user's choice to the function
    
    # Start the questionnaire or import process based on the user's choice
    choice = get_data_source_choice()
    if choice == 'excel':
        # If the user chooses to import from Excel, handle the Excel file import and processing
        excel_file_path = get_excel_file_path(DEFAULT_PATH)
        excel_data = load_excel_data(excel_file_path)
        # ... further processing of excel_data
    else:
        # If the user chooses to input data manually, initiate that process
        data = get_data()
        # ... further processing of data
        

# Ensure that the script only runs when it is not imported as a module
if __name__ == "__main__":
    main()

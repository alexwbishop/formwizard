# main.py
#
# main script

from questionnaire.questionnaire import get_data_source_choice
from questionnaire.questionnaire import initiate_filing_questionnaire
from questionnaire.questionnaire import get_data
from excel_import import get_excel_file_path, DEFAULT_PATH, load_excel_data


def main():
    # Start by greeting the user and setting up the initial questionnaire

    print("Starting main function...")  # This line is for debugging purposes
    # After the initial setup, get the data source choice from the user
    choice = get_data_source_choice()
    initiate_filing_questionnaire()
    
    
    
    
    # Based on the choice, proceed with the Excel import or manual input
    entity_data = get_data(choice)
    
    # Continue with the rest of your script processing the entity data
    if choice == 'excel':
        excel_file_path = get_excel_file_path(DEFAULT_PATH)
        # Once you have the file path, you can load the data
        excel_data = load_excel_data(excel_file_path)
        # ... rest of your code to handle the Excel file

# main script function begins here    
if __name__ == "__main__":
    main()
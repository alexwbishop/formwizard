# main.py
#
# main script

from questionnaire.questionnaire import get_data_source_choice
from questionnaire.questionnaire import initiate_filing_questionnaire
from questionnaire.questionnaire import get_data
from excel_import import get_excel_file_path, DEFAULT_PATH, load_excel_data


def main():
    initiate_filing_questionnaire()  # This will print the welcome message
    choice = get_data_source_choice()
    
    if choice == 'excel':
        excel_file_path = get_excel_file_path(DEFAULT_PATH)
        # Once you have the file path, you can load the data
        excel_data = load_excel_data(excel_file_path)
        # ... rest of your code to handle the Excel file

        entity_data = get_data(choice)
    # Continue with the rest of your script

# main script function begins here    
if __name__ == "__main__":
    main()
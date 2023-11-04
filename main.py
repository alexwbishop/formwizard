# main.py
#
# main script

from questionnaire.questionnaire import run_questionnaire
from questionnaire.questionnaire import get_data_source_choice
from questionnaire.questionnaire import initiate_filing_questionnaire
from questionnaire.questionnaire import get_data
from excel_import import load_excel_file, get_excel_file_path
from excel_import import DEFAULT_PATH



def main():
    initiate_filing_questionnaire()  # This will print the welcome message
    choice = get_data_source_choice()
    entity_data = get_data(choice)
    # Continue with the rest of your script

# main script function begins here    
if __name__ == "__main__":
    main()
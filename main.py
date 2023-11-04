# main.py
#
# main script

from questionnaire.questionnaire import run_questionnaire
from questionnaire.questionnaire import get_data_source_choice
from excel_import import load_excel_file, get_excel_file_path
from excel_import import DEFAULT_PATH



def main():
    choice = get_data_source_choice()
    if choice == 1:
        excel_file_path = get_excel_file_path(DEFAULT_PATH)  # Assuming DEFAULT_PATH is defined
        entity_data = load_excel_file(excel_file_path)  # Here, pass the file path from user input
    elif choice == 2:
        entity_data = run_questionnaire()
    else:
        print("Invalid choice, please select a valid option.")
        main()  # Recall main() to get a valid choice

    # Continue with the rest of your script

if __name__ == "__main__":
    main()


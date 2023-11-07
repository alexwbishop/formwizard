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
import questionnaire
import user_input
import json
from user_input import ask_quantity_of_filings
from excel_import import get_excel_file_path, load_excel_data
from constants.config import DEFAULT_PATH
from enums.residency import determine_residency


# Main function that orchestrates the form handling based on user input
def main(): 
    print("......System warming up......") # FIRST MESSAGE #
    # Display a welcome message
    print("Welcome to FormWizard!") 
    # Prompt user for data source preference at the start
    print("We will now ask how you would like to input your data.")
    # Function to ask the user to choose the data input method (Excel or Manual)
    entity_data = user_input.get_data_source()

# Entry point check to prevent code from executing when imported
if __name__ == "__main__":
    main()
    # Prompt user for data source preference at the start


    
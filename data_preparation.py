# data_preparation.py

# Functions relating to collecting and preparing data for processing and application to forms
from user_input import get_manual_input_data
from classes.ResidencyBase import determine_residency

# asks for number of forms to fill out in current session
def ask_quantity_of_filings() -> int:
    while True:
        try:
            num_forms = int(input("How many forms do you want to fill out today? (max 10): "))
            if 1 <= num_forms <= 10:
                return num_forms
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid number.") 

# Uses existing function to ask the user to provide entity data for the total number of requested forms (not filing data)
def get_data(user_choice):
    # Use the user_choice parameter to determine how to get data.
    if user_choice == 'manual':
        print("Welcome to the FormWizard Manual Info Entry Questionnaire!")
        entity_data = get_manual_input_data()
        # Initialize list to store form instances for each entity/form
        num_forms = []

    # Ensure 'Domestic State' is set
    if 'Domestic State' not in entity_data or not entity_data['Domestic State']:
        entity_data['Domestic State'] = input("Domestic State was not obtained from import. Please provide the domestic state: ")

    # Now that entity_data is fully populated, determine the residency class
    entity_data['Residency Class'] = determine_residency(entity_data['Domestic State'])

    # entity data is loaded into the session, and the session is ready to begin the filing-specific question phase (FormWizard in form_wizard.py)
    return entity_data


# data_preparation.py

# Functions relating to collecting and preparing data for processing and application to forms
from user_input import ask_quantity_of_filings, get_manual_input_data
from classes.ResidencyBase import determine_residency

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

    # entity data is loaded into the session, and the session is ready to begin the filing-specific question phase (FormWizard in questionnaire.py)
    return entity_data


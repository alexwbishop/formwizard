# questionnaire.py

# Initial Session Questions, Entity & Filing Selection
import json
import pandas as pd
from datetime import datetime
from enums.filing_rules import FilingType, FILING_QUESTIONS
from enums.residency import Residency
from enums.entity_types import EntityType
from classes.Jurisdiction import Jurisdiction  
from classes.BaseForm import BaseForm
from user_input import ask_quantity_of_filings, choice
from data_preparation import get_data
from constants.states import State
from validation import validate_data
from classes.Utilities.ValidationUtils.ValidationUtils import handle_errors
from enums.residency import determine_residency
#
# Create a single BaseForm instance with defaults
# this will be instantiated for each form, and additonal requirements
#  are loaded in from higher classes in the hierarchy
# Load configuration from a JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

form_instance = BaseForm(
    domestic_state=config.get('DEFAULTS', {}).get('domestic_state', Jurisdiction.create_jurisdiction("Delaware", "DE")),
    session_timestamp=datetime.now(),
    signed_on_date=datetime.now(),
    jurisdiction_instance=config.get('DEFAULTS', {}).get('jurisdiction_instance', Jurisdiction.create_jurisdiction("Delaware", "DE")),
)

# Create an instance of the Jurisdiction class which allows it to be changed from default (DE)
current_jurisdiction = Jurisdiction.create_jurisdiction(State.full[State.abbrev])
de_jurisdiction = Jurisdiction.create_jurisdiction("Delaware", "DE")
ca_jurisdiction = Jurisdiction.create_jurisdiction("California", "CA")

# Functions

#Tips to improve: You can design a data collection function that accepts data from multiple sources, checks if 
# essential data is missing, and prompts the user only for missing elements.
#For the data that is not mutually exclusive, consider creating a dictionary that holds all the form data, 
# then updating it with data from the Excel file first and subsequently filling in the gaps with user input.

# Uses existing function to ask the user to select number of forms to be filled (up to 10), 
# and sets the number of forms to be filled. 
def initiate_filing_questionnaire():
    print("Welcome to the Filing Questionnaire Session.")
    num_forms = ask_quantity_of_filings()  # This will return an integer
    return num_forms  # Return the number of forms as an integer

# define the core data collection and form assembly process (FormWizard)
class FormWizard:
    def __init__(self):
        self.entities_data = []
        self.filing_data = []    
        
    def run_session(self):
        print("Initializing FormWizard session...")
        # Collect the data for each entity from the user
        for _ in range(ask_quantity_of_filings()):
            entity_data = get_data(choice)
            # Validate and store entity data
            valid, error_message = self.validate_data(entity_data)
            if not valid:
                self.handle_errors(error_message)
                continue  # Skip to the next entity if the current one is invalid
            self.entities_data.append(entity_data)
        
        # Loop for confirming data
        while True:
            self.display_data_for_confirmation()
            if self.confirm_data():
                break
            else:
                self.correct_data()  # You will need to define how to correct data
        
        ## FORM GENERATION PROCESS OCCURS ##
        self.generate_forms()

            # user could be given option to skip data entry of missing fields, then fill post-session manually,
            # but we would want to build in a reminder feature for that.
    def confirm_data(self):
        confirmation = input("Do you confirm the provided data? (Yes/No): ")
        return confirmation.lower() == 'yes'

    def correct_data(self):
    # Logic for correcting data goes here
        pass

# Display the collected data to the user for review - Newly implemented
    def display_and_confirm_data(self):
             for entity in self.entities_data:
                 print(entity)
             for filing in self.filing_data:
                 print(filing)
             # Get user confirmation
             confirmation = input("Do you confirm the provided data? (Yes/No): ")
             if confirmation.lower() == 'yes':
                 return True
             return False
    def generate_forms(self):
        print("Initiating form generation process...")
        form_template_path = f"StateForms/{Jurisdiction}/{Jurisdiction}-{EntityType}-{Residency}-{FilingType}.pdf"
        print("Loaded form: ", form_template_path)  
        # USE PDF FUNCTIONS FROM pdf_utils.py - not being used yet?

    def end_or_continue(self):
        choice = input("Would you like to end the session or continue with another task? (End/Continue): ")
        if choice.lower() == 'end':
            print("Thank you for using FormWizard!")
            return
        # If the user wants to continue, redirect them to the starting point or offer other options

        # entity data error validation
        valid, error_message = self.validate_data(self.entities_data)
        if not valid:
            self.handle_errors(error_message)
            return

        if not self.display_and_confirm_data():
            #if the user says 'no', there should be a mechanism to go back and allow data correction.
            return
        ## FORM GENERATION PROCESS OCCURS ##
        self.generate_forms()

# Usage
if __name__ == "__main__":
    print("questionnaire.py initiated as main.")
    wizard = FormWizard()
    print("Initializing FormWizard session...")
    wizard.run_session()
    print("Session complete.")
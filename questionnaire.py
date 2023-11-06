# questionnaire.py

# Initial Session Questions, Entity & Filing Selection
import pandas as pd
from enums.filing_rules import FILING_TYPES, is_valid_new_name
from enums.filing_rules import FilingType, FILING_QUESTIONS
from classes.Residency import Residency
from enums.entity_types import EntityType
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from main import choice
from user_input import ask_quantity_of_filings, get_manual_input_data
from data_preparation import get_data

# Define 'determine_residency' as a top-level function - because it drives the logic of other class-based functions
# this was refactored to ./classes/Residency/residency.py

# Create an instance of the Jurisdiction class
current_jurisdiction = Jurisdiction.create_jurisdiction(state_name_mapping[state], state)
de_jurisdiction = Jurisdiction.create_jurisdiction("Delaware", "DE")
ca_jurisdiction = Jurisdiction.create_jurisdiction("California", "CA")

# Overwrite form instance attributes as necessary - Not currently implemented
#if some_condition:
#    form_instance.domestic_state = "DE"

# Now that form_instance is defined, you can update de_jurisdiction with it if needed
de_jurisdiction.jurisdiction_instance = form_instance

# Create a single BaseForm instance with defaults
# this will be instantiated for each form, and additonal requirements
#  are loaded in from higher classes in the hierarchy
form_instance = BaseForm(
    domestic_state=DEFAULTS.get('domestic_state', 'DE'), 
    form_status=DEFAULTS.get('form_status', 'Blank'), 
    session_timestamp=datetime.now(), 
    signed_on_date=datetime.now(),
    jurisdiction_instance=de_jurisdiction,
)

# Functions

# Uses existing function to ask the user to select number of forms to be filled (up to 10), 
# and sets the number of forms to be filled.
def initiate_filing_questionnaire():
    print("Welcome to the Filing Questionnaire Session.")
    num_forms = ask_quantity_of_filings()  # This will return an integer
    return num_forms  # Return the number of forms as an integer

# define the core data collection and form assembly process (FormWizard)
class FormWizard:
    def run_session(self):
        print("Initializing FormWizard session...")
        # Collect the data for each entity from the user
        for _ in range(ask_quantity_of_filings()):
            entity_data = get_data(choice) # NOT DEFINED? Waze
            # Validate and store entity data
            valid, error_message = self.validate_data(entity_data)
            if not valid:
                self.handle_errors(error_message)
                continue  # Skip to the next entity if the current one is invalid
            self.entities_data.append(entity_data)
            # user could be given option to skip data entry of missing fields, then fill post-session manually,
            # but we would want to build in a reminder feature for that.
            
    def __init__(self):
        self.entities_data = []
        self.filing_data = []

# # Display the collected data to the user for review - Newly implemented
        def display_data_for_confirmation(self):
             for entity in self.entities_data:
                 print(entity)
             for filing in self.filing_data:
                 print(filing)
             # Get user confirmation
             confirmation = input("Do you confirm the provided data? (Yes/No): ")
             if confirmation.lower() == 'yes':
                 return True
             return False
    
   # Since you mentioned that the coordinates JSON files have moved, you'll need to update the paths to these files in your code once you integrate the PDF generation functionality.
    def generate_forms(self):
        print("Generating forms...")
        form_template_path = f"StateForms/{Jurisdiction}/{Jurisdiction}-{entity_type}-{residency}-{filing_type}.pdf"
        print("Loaded file: ", form_template_path)  

## FORM GENERATION PROCESS OCCURS ##

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

        if not self.display_data_for_confirmation():
            # If the user doesn't confirm the data, give them a chance to modify it
            # ...
            return

        self.generate_forms()



# give user opportunity to exit or restart a new session
def end_or_continue(self):
        self.generate_summary()
        self.collect_feedback()
        
        choice = input("Would you like to end the session or continue with another task? (End/Continue): ")
        if choice.lower() == 'end':
            print("Thank you for using FormWizard! Have a great day.")
            return
        # If the user wants to continue, redirect them to the starting point or offer other options
        # IS THIS DEFINED YET? #
        # self.run_session()     ????

#Usage:
# To start the session:
#wizard = FormWizard()
#wizard.run_session()
# You can call initiate_filing_questionnaire() to start the process
# You can call get_data() to get the data for a single entity
if __name__ == "__main__":
    wizard = FormWizard()
    print("this is the test run of questionnaire.py")
    wizard.run_session()
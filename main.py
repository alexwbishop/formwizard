# FormWizard by Alex Bishop - incyde@riseup.net
# Version 1.0.0.2
# Purpose: Automate the process of filling out Change of Agent forms (Corp, LLC, LP), Domestic and Foreign. in DE and CA.
# main.py

# load external functions
from config_utils import load_json_config
from input_validators import date_time_validation, validate_target_file, validate_confirmation_checks  # Replace with actual function names
from logging_utils import message_logging, create_session_id  # Replace with actual function names
from pdf_utils import get_pdf_dimensions, populate_form, merge_pdfs  # Replace with actual function names
from questions import get_signer_name, collect_entity_info  # Replace with actual function names
from session_utils import display_complete_list  # Replace with actual function names

# Imports
import re
import json
import os
import PyPDF2
import uuid
import logging
from questions import CAQuestion, DEQuestion
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from classes.BaseForm.base_form import BaseForm
from classes.Jurisdiction.jurisdiction import Jurisdiction

## Call functions

# line of questioning by state
if state == "CA":
    question_obj = CAQuestion()
elif state == "DE":
    question_obj = DEQuestion()
question_obj.all_questions()

# message logging function - Moved

# date & time validation - Moved

# JSON configuration function - Moved
def main():
    config = load_json_config("config.json")
    form_config = load_json_config('field_coordinates.json')
VALID_STATES = config.get('VALID_STATES', []) 
ENTITY_TYPES = config.get('ENTITY_TYPES', [])
FILING_TYPES = config.get('FILING_TYPES', [])
ALL_STATES = config.get('ALL STATES', [])
MAX_FORM_QUANTITY = config.get('MAX_FORM_QUANTITY', 10)
VALID_AGENT_NAMES = config.get('VALID_AGENT_NAMES', [])
DEFAULTS = config.get('DEFAULTS', [])


# Validation Function for Confirmation Checks - Moved

# Validate if target file exists - Moved

# Function to get PDF dimensions - Moved

# Function to populate form fields - Moved

# Function to merge text PDF onto blank form - Moved

# Define creation of session id# - Moved

# Create a DE and CA instance of the Jurisdiction class
de_jurisdiction = Jurisdiction.create_jurisdiction("Delaware", "DE")
ca_jurisdiction = Jurisdiction.create_jurisdiction("California", "CA")

# BaseForm: Instantiate to begin storing the inputted data with some default settings
form_instance = BaseForm(
    domestic_state="DE", 
    form_status="Blank", 
    session_timestamp=datetime.now(), 
    signed_on_date=datetime.now(),
    jurisdiction_instance=de_jurisdiction,
)

# Now that form_instance is defined, you can update de_jurisdiction with it if needed
de_jurisdiction.jurisdiction_instance = form_instance

# Merge overlay and form PDFs together - Moved

# Use the defaults
form_instance = BaseForm(
    domestic_state=DEFAULTS.get('domestic_state', 'DE'), 
    form_status=DEFAULTS.get('form_status', 'Blank'), 
    session_timestamp=datetime.now(), 
    signed_on_date=datetime.now(),
    jurisdiction_instance=de_jurisdiction,
)
## PHASE 1 = Basic command line prompt usage:

user_id = "alexander.bishop"
# Greet and Confirm that User is Alex
#while True:
#    user_id = input("Greetings. Please enter your WK username (e.g., 'john.doe'): ")
    # You can add more validation logic here to check the format of the username.
    # For example, you can check if it contains a dot (.) to match the format.
#    if '.' in user_id:
#        break  # Exit the loop if the format is correct
#    else:
#        logging.warning("Invalid format. Please enter a username in the correct format.")

# Ask for password
#password = input("Please enter your password: ")

# Check if the username and password are correct
#if user_id == 'alexander.bishop' and password == 'scarlet':
#    logging.info("Welcome, Alex!")
#except Exception as e:
#    logging.error(f"Access denied. Please check your username and password.")

# Create a session_id for the form prep session - Moved

# Confirm filing type (currently COA only) - Moved

# Ask for number of forms to complete - Moved

# Confirm state of filing - Moved

# Create an instance of the Jurisdiction class based on user input
jurisdiction_instance = Jurisdiction.create_jurisdiction(state_name, state_code)

# Confirm agent name - Moved

# Collect Signer's Name - Moved

# Confirm Signer's Name - Moved

# Initialize list to store form instances
forms = []

# Load applicable jurisdiction names and abbreviations for the form-prep session
#SCARLET# is this redundant? # de_jurisdiction = Jurisdiction("Delaware", "DE")
#SCARLET# is this redundant? # ca_jurisdiction = Jurisdiction("California", "CA")

# Store inputted signature block info into previously initialized BaseForm instance
form_instance.agent_name = agent_name
form_instance.signer_first = signer_first
form_instance.signer_mid = signer_mid
form_instance.signer_last = signer_last
form_instance.signer_name = signer_name
form_instance.sig_conformed = sig_conformed
form_instance.sig_typed = signer_name

### PHASE 1: DATA COLLECTION & VALIDATION ###

## BEGIN GENERAL QUESTIONS FOR ALL STATES ##

# Initialize a list to store entity data
entity_data_list = []

# Collect entity info - Moved
    
# Ask Domestic State - Moved
    
# Ask Filing State - Moved
    
# Calculate Domestic or Foreign Residency (only for this form/filing) - Moved

# Store entity data in a dictionary
entity_data = {
    'entity_name': entity_name,
    'entity_type': entity_type,
    'domestic_state': domestic_state,
    'jurisdiction': jurisdiction,
    'residency': residency
}
## END GENERAL QUESTIONS FOR ALL STATES ##

## BEGIN CALIFORNIA ONLY QUESTIONS ##

# init state-specific questioning as applicable for filings requested
if jurisdiction == 'CA':
    try:
        # Get the regular expression for business_purpose validation
        business_purpose_regex = config['VALIDATION_RULES']['CA_business_purpose']

        # Assuming user_input is the data you want to validate
        user_input = "CA business purpose must be less than 50 characters."

        # Perform the validation
        if re.match(business_purpose_regex, user_input):
            print("Valid input.")
        else:
            print("Invalid input. Must be 1-50 characters.")

    except KeyError:
        logging.error("CA_business_purpose not found in the JSON configuration.")
        
## END CALIFORNIA ONLY QUESTIONS ##

    # Add to list
    entity_data_list.append(entity_data)
    
# Entity & Filing Info Confirmation (Individual) - Moved

# Entity & Filing Info Confirmation (Complete List) - Moved

# Store each set of inputted entity data from the list (up to 10) into the previously initialized BaseForm instance:
    form_instance.signer_first = signer_first
    form_instance.signer_mid = signer_mid
    form_instance.signer_last = signer_last
    form_instance.signer_name = f"{signer_first} {signer_mid} {signer_last}"

# Construct the PDF file path dynamically - Moved

# Check if PDF files exist - Moved

# store the data into the form class
form_instance.entity_name = entity_name,
form_instance.entity_type = entity_type,
form_instance.jurisdiction_instance = None,  # Not in use- can pull class attributes from jurisdiction layer
form_instance.domestic_state = domestic_state,
form_instance.residency = residency,
form_instance.filing_type = filing_type,

# Loop through the total # of filings requested (up to 10) and store each data set into 'forms', then display list
forms.append(form_instance)

# Display a complete list of up to 10 entities & forms to be filled - Moved

# Ask user to confirm info provided for all filings is correct, proceed to next phase - Moved
### END PHASE 1 ###

### PHASE 2: DOCUMENT PREPARATION ###

# Update form_data with user input
form_data = {
    'entity_name': entity_name,
    'agent_name': agent_name,
    'sig_conformed': sig_conformed,
    'signer_name': signer_name
#SCARLET# Help me to add functionality to load the registered agent address in from a separate library, based on selecting CT or NRAI as the agent_name
}

# define the form key for labeling PDF files being processed, e.g. DE-Corp-Dom-COA - Moved

# Run the populate function on the form
populate_form(f'StateForms/{jurisdiction}/{form_key}.pdf', f'StateForms/{jurisdiction}/output_{form_key}.pdf', form_config.get(form_key, {}), form_data)

# Temporary text overlay PDF path
temp_text_pdf_path = f'completed_forms/temp/temp_text_{form_key}.pdf'
#SCARLET# Help me add a command to delete the temp file folder contents at start of next session (with confirmation)

# Populate form with text
populate_form(f'StateForms/{jurisdiction}/{form_key}.pdf', temp_text_pdf_path, form_config.get(form_key, {}), form_data)

# Merge the original form and text PDF
merge_pdfs(f'StateForms/{jurisdiction}/{form_key}.pdf', temp_text_pdf_path, f'completed_forms/{jurisdiction}-{entity_name}_-_{form_key}_Filled.pdf')

# Print quicklist of all forms/entities that were filled out in current session - Moved

# Show success message & goodbye
ging.info(f"Total PDFs filled: {num_forms}. Total errors: 0 \n Successfully completed session.  \n Thank you for using FormWizard!
\n Your session ID is: {session_id}. \n Time Completed: {session_timestamp} \n Have a great day, {user_id}!")

#SCARLET# help me to add a session  txt file export - confirm with user

#SCARLET# prompt for user feedback of experience 1-10

### END OF PHASE 2 ###

if __name__ == "__main__":
    main()

# Done


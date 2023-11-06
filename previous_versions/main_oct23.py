# FormWizard by Alex Bishop - incyde@riseup.net
# Version 1.0.0.3
# Purpose: Automate the process of filling out Change of Agent forms (Corp, LLC, LP), Domestic and Foreign. in DE and CA.
# main.py

#Here's a breakdown of the current structure:
#1. Imports: Various utility functions and classes are imported.
#2. Configuration Loading: The config.json is loaded, and several global constants are set up.
#3. Main Function: An empty main() function is defined.
#4. Jurisdiction Questioning: Depending on the jurisdiction (CA or DE), the appropriate set of questions is triggered.
#5. Logging: A message logging function is called.
#6. Confirmation and Validation: Various functions are called to confirm and validate the user's input.
#7. Form Population: The form is populated based on the user's input.
#8. PDF Manipulation: Functions are called to manipulate the PDFs, such as merging them.
#9. Session Initialization: A session ID is generated, and various session-related attributes are set.
#10. Data Collection and Validation: A series of questions are asked to collect and validate the data for the form.
#11. Document Preparation: The form is prepared based on the collected data.

# Imports
import re
import os
import json
import logging
from datetime import datetime
from config_utils import load_json_config
from input_validators import (validate_date_time, collect_entity_info, display_form_list, get_confirmation, validate_zip, get_residency, calculate_residency, file_exists, log_entity_data_list, prepare_filings, print_quicklist, load_agent_address)
from previous_versions.logging_utils import message_logging, validate_timestamp
from classes.Utilities.PDFUtils.PDFUtils import form_key, clear_temp_folder, check_file_path, get_pdf_dimensions, populate_form, merge_pdfs
from questions import (ask_yes_no, get_signer_name, confirm_filing_type, ask_total_forms, confirm_limited_states, confirm_agent_name, confirm_signer, get_entity_info, get_domestic_state, get_jurisdiction, confirm_filings)
from previous_versions.session_utils import generate_session_id
from classes.jurisdiction.jurisdiction import Jurisdiction
from classes.BaseForm.BaseForm import BaseForm
def main():
    def setup_config():
        config = load_json_config("config.json")
        FILING_TYPES = config['FILING_TYPES']
        MAX_FORM_QUANTITY = config['MAX_FORM_QUANTITY']
        VALID_STATES = config['VALID_STATES']
        ENTITY_TYPES = config['ENTITY_TYPES']
        ALL_STATES = config['ALL STATES']
    return FILING_TYPES, MAX_FORM_QUANTITY, VALID_STATES, ENTITY_TYPES, ALL_STATES

# For Jurisdiction Handling:
jurisdiction_value = get_jurisdiction()  # Assuming get_jurisdiction() returns the jurisdiction value

# begin line of questioning for filing jurisdiction
if Jurisdiction == "CA":
    question_obj = CAQuestion()
elif Jurisdiction == "DE":
    question_obj = DEQuestion()
else:
    print("Unexpected jurisdiction value entered.")
    # You can handle the unexpected input here, such as raising an exception or providing a default behavior.

if Jurisdiction in ["CA", "DE"]:
    question_obj.all_questions()

# message logging function
message_logging()
get_signer_name()

# Validation Function for Confirmation Checks
get_confirmation()
# Validate if target file exists
form_template_path = f"StateForms/{Jurisdiction}/{Jurisdiction}-{entity_type}-{residency}-{filing_type}.pdf"
check_file_path(form_template_path)
# Function to get PDF dimensions
get_pdf_dimensions(pdf_path)
# Function to populate form fields
populate_form()
# Function to merge text PDF onto blank form
merge_overlay_pdf()
# Create an instance of the Jurisdiction class
current_jurisdiction = Jurisdiction.create_jurisdiction(state_name_mapping[state], state)
#de_jurisdiction = Jurisdiction.create_jurisdiction("Delaware", "DE")
#ca_jurisdiction = Jurisdiction.create_jurisdiction("California", "CA")

# Create a single BaseForm instance with defaults
form_instance = BaseForm(
    domestic_state=DEFAULTS.get('domestic_state', 'DE'), 
    form_status=DEFAULTS.get('form_status', 'Blank'), 
    session_timestamp=datetime.now(), 
    signed_on_date=datetime.now(),
    jurisdiction_instance=de_jurisdiction,
)

# date & time validation - not used
#date_time_input = input("Enter date and time (format: YYYY-MM-DD HH:MM:SS): ")
#
#if validate_date_time(date_time_input):
#    print("Valid date and time!")
#else:
#    print("Invalid date and time format!")

# Overwrite form instance attributes as necessary
if some_condition:
    form_instance.domestic_state = "DE"

# Now that form_instance is defined, you can update de_jurisdiction with it if needed
de_jurisdiction.jurisdiction_instance = form_instance

# Merge overlay and form PDFs together - Moved
merge_pdfs()

# Use the defaults
form_instance = BaseForm(
    domestic_state=DEFAULTS.get('domestic_state', 'DE'), 
    form_status=DEFAULTS.get('form_status', 'Blank'), 
    session_timestamp=datetime.now(), 
    signed_on_date=datetime.now(),
    jurisdiction_instance=de_jurisdiction,
)
## PHASE 1 = Basic command line prompt usage:

# user login with password - disabled
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

# Create a session_id for the form prep session
session_id = generate_session_id()
#  assign the user_id and timestamp to the session markers
form_instance.user_id = user_id
form_instance.session_id = session_id
form_instance.session_timestamp = datetime.now()
logging.info(f"Thank you for authenticating, {user_id},! \n Form prep session initialized. \n Username: {user.id},\n Session ID:{session_id} Timestamp: {session_timestamp}")

# Confirm filing type (currently COA only)
confirm_filing_type()
# Ask for number of forms to complete
def ask_total_forms():
    while True:
        try:
            num_forms = int(input(f"How many forms would you like to prepare for this session? (Up to 10): "))
            if 1 <= num_forms <= MAX_FORM_QUANTITY:
                return num_forms
            logging.warning(f"Please enter a number between 1 and {MAX_FORM_QUANTITY}.")
        except ValueError:
            logging.warning("Invalid input. Please enter a number.")

def get_entity_info(num_forms):  # <-- note the argument here
    entities = []
    for i in range(num_forms):
        # Entity Name
        entity_name = input(f"Enter the full name of entity {i+1} of {num_forms}, including corporate indicator: ")
        entities.append(entity_name)
    return entities  # or whatever data structure you want to use to store this information

def main():
    FILING_TYPES, MAX_FORM_QUANTITY, VALID_STATES, ENTITY_TYPES, ALL_STATES = setup_config()

# Create an instance of the Jurisdiction class based on user input
jurisdiction_value = get_jurisdiction()
jurisdiction_instance = Jurisdiction.create_jurisdiction(state_name, state_code)

# Confirm agent name
confirm_agent_name()
# Collect Signer's Name
get_signer_name()
# Confirm Signer's Name
confirm_signer()
# Initialize list to store form instances
forms = []

# Load applicable jurisdiction names and abbreviations for the form-prep session
#de_jurisdiction = Jurisdiction("Delaware", "DE")
#ca_jurisdiction = Jurisdiction("California", "CA")

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

# Collect entity info
collect_entity_info()
get_domestic_state()
get_jurisdiction(entity_name)
    
# Calculate Domestic or Foreign Residency (only for this form/filing)
get_residency()

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
    
# Entity & Filing Info Confirmation
display_form_list()

# Store each set of inputted entity data from the list (up to 10) into the previously initialized BaseForm instance:
form_instance.signer_first = signer_first
form_instance.signer_mid = signer_mid
form_instance.signer_last = signer_last
form_instance.signer_name = f"{signer_first} {signer_mid} {signer_last}"

# Check if PDF files exist
check_file_path()

# store the data into the form class
form_instance.entity_name = entity_name,
form_instance.entity_type = entity_type,
form_instance.jurisdiction_instance = None,  # Not in use- can pull class attributes from jurisdiction layer
form_instance.domestic_state = domestic_state,
form_instance.residency = residency,
form_instance.filing_type = filing_type,

# Loop through the total # of filings requested (up to 10) and store each data set into 'forms', then display list
forms.append(form_instance)

# Display confirmation list of up to 10 entities & forms to be filled
display_form_list()

# Ask user to confirm info provided for all filings is correct, proceed to next phase
confirm_filings()

### END PHASE 1 ###

### PHASE 2: DOCUMENT PREPARATION ###

# Update form_data with user input
form_data = {
    'entity_name': entity_name,
    'agent_name': agent_name,
    'sig_conformed': sig_conformed,
    'signer_name': signer_name
}

# load stored agent address based on selection of agent_name
if agent_name in ["CT", "NRAI"]:
    agent_address = load_agent_address(agent_name)
    form_data['agent_address'] = agent_address

# Run the populate function on the form
populate_form(f'StateForms/{jurisdiction}/{form_key}.pdf', f'StateForms/{jurisdiction}/output_{form_key}.pdf', form_config.get(form_key, {}), form_data)

# Temporary text overlay PDF path
temp_text_pdf_path = f'completed_forms/temp/temp_text_{form_key}.pdf'

# Populate form with text
populate_form(f'StateForms/{jurisdiction}/{form_key}.pdf', temp_text_pdf_path, form_config.get(form_key, {}), form_data)

# Merge the original form and text PDF
merge_pdfs(f'StateForms/{jurisdiction}/{form_key}.pdf', temp_text_pdf_path, f'completed_forms/{jurisdiction}-{entity_name}_-_{form_key}_Filled.pdf')

# Print quicklist of all forms/entities that were filled out in current session - Moved
display_complete_list()

# Show success message & goodbye
logging.info(f"Total PDFs filled: {num_forms}. Total errors: 0 \n Successfully completed session.  \n Thank you for using FormWizard!\n Your session ID is: {session_id}. \n Time Completed: {session_timestamp} \n Have a great day, {user_id}!")

# prompt user to delete the temp file folder contents (with confirmation)
clear_temp_folder()

# session  txt file export - confirm with user
def export_session_to_txt(session_id, user_id, session_timestamp, num_forms):
    with open(f'session_{session_id}.txt', 'w') as file:
        file.write(f"Username: {user_id}\n")
        file.write(f"Session ID: {session_id}\n")
        file.write(f"Timestamp: {session_timestamp}\n")
        file.write(f"Total PDFs filled: {num_forms}\n")
    print("Session details exported to txt file.")
    # Confirm with user
    confirmation = input("Do you want to view the exported session details? (yes/no): ")
    if confirmation.lower() == 'yes':
        with open(f'session_{session_id}.txt', 'r') as file:
            print(file.read())

# prompt for user feedback of experience 1-10
def get_user_feedback():
    while True:
        try:
            feedback = int(input("On a scale of 1-10, how would you rate your experience? "))
            if 1 <= feedback <= 10:
                return feedback
            print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")


if __name__ == "__main__":
    main()
    
### END OF PHASE 2 ###



# Done


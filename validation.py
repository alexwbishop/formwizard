# validation.py
#
# User Inputs and Validations

# Imports
import re
import json
import os
import uuid
import logging
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from constants.name_restrictions import RESTRICTED_WORDS
from constants.entity_indicators import VALID_ENTITY_INDICATORS
from constants.name_restrictions import MAX_PURPOSE_LENGTH
from datetime import datetime
from enums.residency import Residency
from enums.entity_types import EntityType
import classes.BaseForm.BaseForm
from questionnaire import FormWizard
import questionnaire

# Dalia's tips: 
#Error Handling: Add try-except blocks where appropriate to handle unexpected input.
#Case Sensitivity: Functions like is_valid_entity_name and is_valid_purpose should ideally handle words in a case-insensitive manner.
#Modularity: Consider breaking down some functions further if they start to handle too complex logic.

# Load configuration from a JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Calculate Domestic or Foreign Residency (only for this form/filing)
def get_residency() : 'Dom' if config.Jurisdiction == config.Domestic_State else 'For'

# Entity & Filing Info Prompt
def collect_entity_info():
    while True:
        entity_name, domestic_state, entity_type, filing_type, agent_name, jurisdiction = get_entity_info()
# Confirmation - Individual entity/form info
        if get_confirmation(f"Entity info entered: {entity_name} (a {domestic_state} {entity_type}) is filing a {filing_type} to {agent_name} in {jurisdiction}. Is this correct? (Y/N): "):
            return entity_name, domestic_state, entity_type, filing_type, agent_name, jurisdiction
        else:
            logging.warning("Please re-enter the entity details.")

# Confirmation - group entity/form info
def display_form_list():
    logging.info(f"List of entities/forms to be filled in this session: ")
    for i, FILING_TYPES in enumerate(FILING_TYPES):
        logging.info(f"{i+1}) form.entity_name - form.entity_type - form.filing_type")

# Ask user to confirm info provided for all filings is correct, proceed
def confirm_filings():
    while True:
        num_forms, form_list = gather_filing_details()
        if get_confirmation(f"All information for form preparation request has been obtained, we are ready to complete {num_forms} forms now. Proceed? (Y/N): "):
            return num_forms, form_list
        else:
            logging.warning("Please restart the session with the correct information.")

# Display a list of all forms/entities that were filled out in current session
def display_complete_list():
    for i, data in enumerate(entity_data_list):
        logging.info(f"PDF for: {data['entity_name']} - {data['jurisdiction']} {data['residency']} {data['entity_type']},) {data['filing_type']}.")

## applied only if registered agent is an individual or non-CT entity (this is rare)
# consider edge cases where a valid individual's name might have more than two components, 
# such as those including a middle name, hyphenated last name, or titles.
def is_valid_agent_name(agent_name: str) -> bool:
    words = agent_name.split()
    # If there's more than one word but less than three, we assume it's a person's name
    if 1 < len(words) <= 2:
        return True
    # Otherwise, we check for business entity indicators
    elif any(indicator in agent_name for indicator in VALID_ENTITY_INDICATORS):
        return True
    else:
        print("Agent name does not seem to be a valid individual or business entity name.")
        return False
    
# validates that business purpose is not too long and does not contain restricted words
# checks for the length of the purpose and restricted words. It’s thorough in its current form. 
# Make sure that RESTRICTED_WORDS is comprehensive and up to date.
def is_valid_purpose(purpose: str) -> bool:
    if len(purpose) > MAX_PURPOSE_LENGTH:
        print("Business purpose is too long.")
        return False
    for word in RESTRICTED_WORDS:
        if word in purpose:
            print(f"'{word}' is a restricted word for business purpose.")
            return False
    return True

# validates that entity name contains a valid entity indicator and does not contain restricted words
# checks for the presence of valid entity indicators and restricted words, which is great. 
# Consider implementing case-insensitive checks to enhance robustness. 
# Right now, it might miss a word if it's capitalized differently.

# validates that entity name is not empty or a duplicate
def check_duplicate_entity(entity_name: str, existing_names: list) -> bool:
    # Check for empty string or only whitespace
    if not entity_name.strip():
        return False
    # Check for duplicates
    if entity_name in existing_names:
        return False
    # Include additional rules if necessary
    return True

# validates that entity name contains a valid entity indicator and does not contain restricted words
def is_valid_entity_name(entity_name: str) -> bool:
    if not any(indicator in entity_name for indicator in VALID_ENTITY_INDICATORS):
        print("Entity name must include a valid entity indicator (e.g., LLC, Inc., Corp.).")
        return False
    for word in RESTRICTED_WORDS:
        if word in entity_name:
            print(f"'{word}' is a restricted word for entity names.")
            return False
    return True

# validates that formation date is a valid date using Python's datetime library for date validation.
def is_valid_formation_date(date_str: str) -> bool:
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # assuming date format as 'YYYY-MM-DD'
        if datetime(1900, 1, 1) <= date_obj <= datetime.today():
            return True
        print("Invalid date. Please provide a date between 1900 and today.")
        return False
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
        return False

# validate signer title matches with entity type
def is_valid_signer_title(entity_type: str, title: str) -> bool:
    if title not in ENTITY_TITLE_MATCH.get(entity_type, []):
        print(f"'{title}' is not a valid title for {entity_type}.")
        return False
    return True

# validate signer name is an individual's name
def is_valid_signer_name(name: str) -> bool:
    if 1 < len(name.split()) <= 2:  # expecting a first and last name
        return True
    print("Signer name does not seem to be a valid individual's name.")
    return False

def get_signer_details(entity_type):
    signer_name = input("Please enter the signer's name: ")

    # Providing title options based on entity type
    if entity_type == 'Corporation':
        print("Select the title or write in your own:")
        print("1. President")
        print("2. Vice President")
        print("3. Secretary")
        print("4. Other (Write-in)")

        choice = input("Enter choice: ")
        if choice == '4':
            signer_title = input("Enter the custom title: ")
        else:
            titles = ["President", "Vice President", "Secretary"]
            signer_title = titles[int(choice)-1]

    elif entity_type == 'LLC':
        print("Select the title:")
        print("1. Manager")
        print("2. Member")
        print("3. Authorized Person")

        choice = input("Enter choice: ")
        titles = ["Manager", "Member", "Authorized Person"]
        signer_title = titles[int(choice)-1]

    return signer_name, signer_title

def handle_multiple_signers(entity_count, entity_type):
    same_signer = input("Is it the same signer for all forms? (yes/no) ")

    signers_list = []

    if same_signer.lower() == 'yes':
        signer_name, signer_title = get_signer_details(entity_type)
        signers_list.append((signer_name, signer_title))

    else:
        for i in range(entity_count):
            print(f"Enter details for signer of entity {i+1}")
            signer_name, signer_title = get_signer_details(entity_type)
            signers_list.append((signer_name, signer_title))

    return signers_list

from datetime import datetime, timedelta

def get_signature_date():
    apply_signature = input("Do you want to apply the conformed signature to the form? (yes/no) ")
    if apply_signature.lower() == 'yes':
        date_format = "%Y-%m-%d"
        today = datetime.today()

        while True:
            chosen_date = input(f"Please enter the desired signature date (format: {date_format}): ")
            chosen_datetime = datetime.strptime(chosen_date, date_format)

            if today <= chosen_datetime <= (today + timedelta(days=90)):
                return chosen_date
            else:
                print(f"Date should be between {today.strftime(date_format)} and {(today + timedelta(days=90)).strftime(date_format)}")
    else:
        return None

def validate_data(self, data):
        # Implement data validation here
        # For example: 
        # if not data['entity_name']:
        #     return False, "Entity name is missing."
        # ... and so on for other validations
        # validation of answers to questions specific to the filing type
        def handle_changeofagent():
        # e.g. for Change of Agent, if we needed prior Registered agent info, we would want to validate that it's not the same as current agent
        # info, however currently supported state and filing types (DE) does not need prior agent info
            pass
            
        def handle_incorporation():
            pass

        def handle_registration():
            pass

        def handle_qualification():
            pass

        def handle_withdrawal():
            pass

        def handle_cancellation():
            pass

        def handle_reinstatement():
            pass

            # how to check if the new name is valid
        def handle_nameamendment(current_name: str):
            print(f"validating {current_name}...")
            # Ask for the new name
            new_name = input(FILING_QUESTIONS[FilingType.NAME_AMENDMENT][0])
            # Validate the new name
            while not is_valid_new_name(current_name, new_name):
                # Ask for the new name again if it's invalid
                new_name = input(FILING_QUESTIONS[FilingType.NAME_AMENDMENT][0])
            # Store the new name or process it as needed
            # DALIA #  DO I NEED TO PUT A return HERE for it to send the validation back to the main function?
            pass

        def handle_stockamendment():
            pass

        def handle_annualreport():
            pass

        def handle_addressupdate():
            pass

        def handle_officialsupdate():
            pass

        def handle_merger():
            pass

        def handle_conversion():
            pass

        def handle_dissolution():
            pass

        def handle_correction():
            pass

        def handle_businesslicense():
            pass

        def handle_miscfiling():
            pass
        
        return True, ""

    
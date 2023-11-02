# input validators.py
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

# functions

# Validate date and time
def validate_date_time(date_time_str, format_str='%Y-%m-%d %H:%M:%S'):
    """
    Validates if the provided string conforms to the specified date and time format.
    
    Parameters:
    - date_time_str (str): The date and time string to validate.
    - format_str (str, optional): The format against which to validate the string. Default is '%Y-%m-%d %H:%M:%S'.

    Returns:
    - bool: True if the string is a valid date and time. False otherwise.
    """
    try:
        datetime.datetime.strptime(date_time_str, format_str)
        return True
    except ValueError:
        return False

# Validation Function for Confirmation Checks
def get_confirmation(prompt: str, error_msg: str = "Invalid input. Please try again.") -> bool:
    while True:
        try:
            confirmation = input(prompt).lower()
            if confirmation == 'y':
                return True
            elif confirmation == 'n':
                return False
            else:
                print(error_msg)
        except Exception as e:
            logging.error(str(e))

# Calculate Domestic or Foreign Residency (only for this form/filing)
def get_residency() : 'Dom' if jurisdiction == domestic_state else 'For'

# Validate if target file exists
def file_exists(filepath):
    try:
        return os.path.isfile(filepath)
    except Exception as e:
        logging.error(f"An error occurred:, {e}")
        return False

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
    for i, form in enumerate(forms):
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
        logging.info(f"PDF for: {data['entity_name']} - {data['jurisdiction']} {data['residency']} 
          {data['entity_type']},) {data['filing_type']}.")

# ZIP code validation (not yet being used)
def validate_zip():
  while True:
    agent_zip = input("Enter the agent's ZIP code: ")
  while not agent_zip.isdigit() or len(agent_zip) != 5:
    agent_zip = input("Enter a valid ZIP code: ")

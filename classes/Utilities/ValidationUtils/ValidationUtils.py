# validationutils.py
import re
import json
import os
import uuid
import logging
import datetime
from constants.config import DEFAULT_PATH
from constants.states import State
from BaseForm import DomesticState

# various utility functions for validation and error handling

# Load configuration from a JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# basic error handling function - needs to be expanded
def handle_errors(self, error):
    print(f"An error occurred: {error}")
    # Additional error handling can be implemented here

# ZIP code validation (not yet being used)
def validate_zip():
  while True:
    agent_zip = input("Enter the agent's ZIP code: ")
  while not agent_zip.isdigit() or len(agent_zip) != 5:
    agent_zip = input("Enter a valid ZIP code: ")

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
    
# date & time validation
def validate_timestamp():
    from datetime import datetime
    try:
        current_time = datetime.now()
        logging.info(f"Current time: {current_time}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

## checks if the address being provided is within the state being filed (jurisdiction).
def instate_address(address: str) -> bool:
    if DomesticState not in address: # need to make this a variable for the jurisdiction abbreviation
        print("Address must be in the state of ", DomesticState, ".")
        return False
    # Other address validations can be added here
    return True

# Validate if target file exists
def file_exists(filepath):
    try:
        return os.path.isfile(filepath)
    except Exception as e:
        logging.error(f"An error occurred:, {e}")
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
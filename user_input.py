# user_input.py
import re
import json
import os
import uuid
import logging
import datetime

# Load configuration from a JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Functions relating to receiving and validating user input 
from constants.states import VALID_STATES
from classes.BaseForm import BaseForm
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

# Helper function to format confirmation prompts
def get_confirmation(prompt):
    return input(prompt).strip().lower() in ['y', 'yes']

# Helper function to get the signer's name - this needs to be defined elsewhere
def get_signer_name():
    return input("Please enter the signer's full name: ")

# Confirm Signer's Name
def confirm_signer():
    while True:
        signer_name = get_signer_name()  # Get the signer's name
        # Confirm the signer's name
        if get_confirmation(f"Signer's full name is {signer_name}. Is this correct? (Y/N): "):
            logging.info(f"Signer's name confirmed as {signer_name}")
            return signer_name  # Return the confirmed signer name
        else:
            logging.warning("Signer's name not confirmed. Asking for re-entry.")

# Confirm filing type availability is limited (currently COA only)
def confirm_filing_type():
    while True:
        filing_type = input(f"Note: FormWizard only supports form completion for 'Change of Agent' at this time. Please confirm (COA): ")
        if filing_type in config.FILING_TYPES:
            break
        else:
            logging.warning("Only Change of Agent filing type is currently supported.\n Please check back later for more filing types in the future or enter 'COA' to proceed.")

# Confirm limited # of states are currently supported
def confirm_limited_states():
    while True:
        state_code = input("FormWizard currently supports filings for Delaware (DE) only. Please enter the corresponding state code (DE/CA): ").upper()
        if state_code in config.ALL_STATES:
            state_name = config.SUPPORTED_STATES[state_code]
            break
        logging.warning("Sorry, we currently only support filings for Delaware (DE). Please check back later for more states.")
        return state_code
    
# Confirm agent name
def get_registered_agent_name(state):
    return config.VALID_AGENTS['VALID_AGENTS'].get(state)

def confirm_agent_name(state):
    # Fetch agent names dynamically based on the state
    valid_agent_names = config.VALID_AGENT_NAMES['VALID_AGENT_NAMES'].get(state, [])

    while True:
        logging.info("Please select the agent name from the list of valid options:")
        for i, name in enumerate(config["VALID_AGENT_NAMES"], 1):
            logging.info(f"{i}. {name}")
        try:
            selection = int(input("Enter the number corresponding to your choice: "))
            if 1 <= selection <= len(valid_agent_names):
                agent_name = valid_agent_names[selection - 1]
                break
            else:
                logging.warning("Invalid selection. Please choose a number from the list.")
        except ValueError:
            logging.warning("Invalid input. Please enter a number.")
    logging.info(f"You've selected {agent_name} as the agent.")
    return agent_name  # Optionally return the agent name for future use


def get_manual_input_data():
    print("Please provide the following info: ")
    data = {}
    data['Entity Name'] = input("Enter Entity Name: ")
    data['Domestic State'] = input("Enter the domestic state: ")
    #data['Current Registered Agent'] = input("Enter current registered agent: ") # make this into a selection from a list
    #data['Current Agent Address'] = input("Enter current agent's address: ") # make this into a selection from a list



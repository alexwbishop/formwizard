# user_input.py
import re
import json
import os
import logging
from constants.states import VALID_STATES
from classes.BaseForm import BaseForm
from enums.residency import determine_residency
from excel_import import import_from_excel
from data_preparation import get_data

# Load configuration from a JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
try:
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    logging.error("config.json file not found.")
    exit(1)
except json.JSONDecodeError:
    logging.error("config.json is not a valid JSON file.")
    exit(1)

# Uses existing function to ask the user to select number of forms to be filled (up to 10), 
# and sets the number of forms to be filled.
# This function now accepts 'num_forms' as a parameter instead of calling 'ask_quantity_of_filings'
def initiate_filing_questionnaire(user_choice, num_forms):
    print("Welcome to the Filing Questionnaire Session.")
    # Use 'num_forms' that was passed as a parameter
    # Depending on the user_choice, get the data source
    data_source = get_data_source(user_choice, num_forms)

# This function now also accepts 'num_forms' as a parameter
def get_data_source(user_choice, num_forms):
    if user_choice == 'excel':
        # Handle the Excel input method
        return import_from_excel()
    elif user_choice == 'manual':
        # Handle the manual input method
        print("You have chosen to input data manually.")
        # We no longer need to ask for the number of forms here since it's passed as a parameter
        # Loop to process each form as per the number specified
        for _ in range(num_forms):
            # Gather data manually for each form
            entity_data = get_data(user_choice)
            # Determine and assign residency status based on the domestic state provided
            print("Determining residency based on data provided...")
            domestic_state = entity_data['Domestic State']
            entity_data['Residency'] = determine_residency(domestic_state)
            print("Residency determined successfully: " + entity_data['Residency'])
            # Additional steps to process each manually entered 'entity_data' can be done here
    else:
        # Handle other cases or raise an error
        print("Invalid choice. Please choose 'excel' or 'manual'.")
        return None

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
        if filing_type == 'COA':
            return filing_type
        else:
            print("Invalid input. Currently, only 'Change of Agent' (COA) is supported.")


# Confirm limited # of states are currently supported
def confirm_limited_states():
    while True:
        state_code = input("FormWizard currently supports filings for Delaware (DE) only. Please enter the corresponding state code (DE/CA): ").upper()
        if state_code == 'DE':
            return state_code
        else:
            print("Invalid input. Currently, only filings for Delaware (DE) are supported.")

    
# use this once other states are added besides DE #
'''def confirm_limited_states():
    while True:
        state_code = input("FormWizard currently supports filings for Delaware (DE) only. Please enter the corresponding state code (DE/CA): ").upper()
        if state_code in config.ALL_STATES:
            state_name = config.SUPPORTED_STATES[state_code]
            break
        #ADD: provide a clear message to the user about what was correct or incorrect.
        logging.warning("Sorry, we currently only support filings for Delaware (DE). Please check back later for more states.")
        return state_code
'''    
# Confirm agent name
def get_registered_agent_name(state):
    return config.VALID_AGENTS['VALID_AGENTS'].get(state)

# FIX: confirm_agent_name, ensure that the dynamic data such as valid agent names are fetched and presented correctly.

# The current code snippet seems to be incomplete as it does not show how the VALID_AGENT_NAMES is structured within the configuration.
def confirm_agent_name(state):
    # Fetch agent names dynamically based on the state
    valid_agent_names = config['VALID_AGENT_NAMES'][state]  # Assuming this returns a list of names
    for i, name in enumerate(valid_agent_names, 1):
        print(f"{i}. {name}")
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

# can add a helper function that can be used for both the agent and the address
def get_manual_input_data():
    print("Please provide the following info: ")
    data = {}
    data['Entity Name'] = input("Enter Entity Name: ")
    data['Domestic State'] = input("Enter the domestic state: ")
    #data['Current Registered Agent'] = input("Enter current registered agent: ") # make this into a selection from a list
    #data['Current Agent Address'] = input("Enter current agent's address: ") # make this into a selection from a list



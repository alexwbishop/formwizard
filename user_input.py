# user_input.py
import re
import json
import os
import uuid
import logging
import datetime
from excel_import import get_excel_file_path, load_excel_data

# Load configuration from a JSON file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Functions relating to receiving and validating user input 
from constants.states import VALID_STATES
from classes.BaseForm import BaseForm

def get_data_source(choice):
        # Prompt user for data import method, store the response in 'choice'
        choice = input("Would you like to import data from an Excel sheet (type 'excel') or input manually (type 'manual')? ")
        # Loop to ensure a valid response is entered
        while choice not in ['excel', 'manual']:
            print("Invalid choice. Please choose 'excel' or 'manual'.")
            choice = input("Would you like to import data from an Excel sheet or input manually? ")
        # Return the user's choice to the calling function
        return choice
        if choice == 'Excel':
        # Handle the Excel input method
            print("You have chosen to import data from an Excel sheet. Please have your file path name ready to enter.")
            # Retrieve the path to the Excel file based on a default or user-provided path
            excel_file_path = get_excel_file_path(DEFAULT_PATH)
            # Load the data from the Excel file into 'entity_data'
            print("Loading data from Excel file...")
            entity_data = load_excel_data(excel_file_path)
            print("Data loaded. Validating...")
            # Send data to LOG FILE with import & Validation details?
            #entity_data = validate_entity_data(entity_data) 
            # Need to set up validate_entity_data function to check for completeness and correctness of the data.
            if not entity_data:  # If validation fails, handle it appropriately
                print("Invalid data found in Excel. Please correct the data and try again.")
        # Additional processing of the data from the Excel file can occur here
        elif choice == 'Manual':
        # Handle the manual input method
            print("You have chosen to input data manually.")
            # Launch the questionnaire to determine the number of forms to process
            print("Booting up filing questionnaire. Please wait...")
            num_forms = initiate_filing_questionnaire() 
            # Loop to process each form as per the number specified
            for _ in range(num_forms):
            # Gather data manually for each form
                entity_data = get_data()
# DALIA HELP - Can the below be replaced with a call to determine_residency function in questionnaire.py?
            # Determine and assign residency status based on the domestic state provided
            print("Determining residency based on data provided...")
            domestic_state = entity_data['Domestic State']
            entity_data['Residency'] = determine_residency(domestic_state)
            print("Residency determined successfully: " + entity_data['Residency'])
            # Additional steps to process each manually entered 'entity_data' can be done here
        else:
        # Handle other cases or raise an error
            print("Invalid choice. Please choose 'Excel' or 'Manual'.")

''' OLD CODE FOR ABOVE:
    # Prompt user for data import method, store the response in 'choice'
    choice = input("Would you like to import data from an Excel sheet (type 'excel') or input manually (type 'manual')? ")
    # Loop to ensure a valid response is entered
    while choice not in ['excel', 'manual']:
        print("Invalid choice. Please choose 'excel' or 'manual'.")
        choice = input("Would you like to import data from an Excel sheet or input manually? ")
    # Return the user's choice to the calling function
    print("Data source selected: " + choice)
    return choice
'''    


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



# questions.py
# Questions and State Handling

#Steps to Populate questions.py:
    #Identify Question Points: Scan your current codebase to identify where you're asking for user input. This can be as simple as calls to input() or more complex UI components.
    #Generalize Questions: If you notice that you're asking similar types of questions across the board, you could generalize them into a single function.
#For example, if you have multiple Yes/No questions, you could have a general ask_yes_no_question() function.
    #Validation Functions: If you have validation logic right next to the question prompt, consider abstracting these into separate functions and moving them into questions.py.
    #State-Specific Questions: Since you have a hierarchy that goes from BaseForm up to Jurisdiction and FilingType,
  #consider adding methods in your Question class (or its subclasses) that generate state or filing type-specific questions.
    #Inheritance and Overriding: If different jurisdictions have slightly different requirements for the same kind of question,
#use inheritance to create a base version of the question in the Question class, and override it in each state-specific subclass as needed.

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

# functions moved in from main.py #

# Collect signer's name
def get_signer_name():
    signer_first = input("Enter the signer's first name: ")
    signer_mid = input("Enter the signer's middle name or initial, if any: ")
    signer_last = input("Enter the signer's last name: ")
    return f"{signer_first} {signer_mid} {signer_last}"


# Confirm filing type (currently COA only)
while True:
    filing_type = input(f"Note: FormWizard only supports form completion for 'Change of Agent' at this time. Please confirm (COA): ")
    if filing_type in FILING TYPES:
        form_instance.filing_type = filing_type
        break
    else:
        logging.warning("Only Change of Agent filing type is currently supported.\n
        Please check back later for more filing types in the future.")

# Ask for number of forms to complete
while True:
    try:
        num_forms = int(input("How many forms would you like to prepare for this session? (Up to 10): "))
        if 1 <= num_forms <= MAX_FORM_QUANTITY:
            break
        logging.warning(f"Please enter a number between 1 and {MAX_FORM_QUANTITY}.")
    except ValueError:
        logging.warning("Invalid input. Please enter a number.")

# Confirm state of filing
while True:
    state_code = input("FormWizard currently supports filings for Delaware (DE) and California (CA) only. Please enter the corresponding state code (DE/CA): ").upper()
    if state_code in VALID_STATES:
        state_name = VALID_STATES[state_code]
        break
    logging.warning("Sorry, we currently only support filings for Delaware (DE) and California (CA). Please check back later for more states.")

# Confirm agent name
while True:
    logging.info("Please select the agent name from the list of valid options:")
    for i, name in enumerate(VALID_AGENT_NAMES, 1):
        logging.info(f"{i}. {name}")
    try:
        selection = int(input("Enter the number corresponding to your choice: "))
        if 1 <= selection <= len(VALID_AGENT_NAMES):
            agent_name = VALID_AGENT_NAMES[selection - 1]
            break
        else:
            logging.warning("Invalid selection. Please choose a number from the list.")
    except ValueError:
        logging.warning("Invalid input. Please enter a number.")
logging.info(f"You've selected {agent_name} as the agent.")
    
# Collect Signer's Name
signer_first = input("Enter the signer's first name: ")
signer_mid = input("Enter the signer's middle name or initial, if any: ")
signer_last = input("Enter the signer's last name: ")
signer_name = f"{signer_first} {signer_mid} {signer_last}"
sig_conformed = f"/s/{signer_name}"

# Confirm Signer's Name
while True:
    signer_name = get_signer_name()
    if get_confirmation(f"Signer's full name is {signer_name}. Is this correct? (Y/N): "):
        logging.info(f"Signer's name confirmed as {signer_name}")
        break
    else:
        logging.warning("Signer's name not confirmed. Asking for re-entry.")

# Collect entity info
for i in range(num_forms):
    # Entity Name
    entity_name = input(f"Enter the full name of entity {i+1} of {num_forms}, including corporate indicator: ")
    
    # Entity Type -  # add action to attempt to guess at the entity_type by scanning through the entity_name
    while True:
        entity_type = input(f"Enter the entity type for {entity_name}: (LLC/Corp/LP): ")
        if entity_type in ENTITY_TYPES:
            break
        else:
            logging.warning("Invalid entity type, or type is not supported. Please select from the approved list (LLC/Corp/LP) again.")
    
# Domestic State
    while True:
        domestic_state = input(f"Enter the domestic state for {entity_name}: (i.e. DE, CA): ")
        if domestic_state in ALL_STATES:
            break
        else:
            logging.warning("Invalid state. Please enter again.")
    
# Filing State
    def get_jurisdiction(entity_name: str) -> str:
    while True:
        jurisdiction = input(f"Enter the state that {entity_name} will file in (i.e. DE, CA): ").upper()
        if jurisdiction in VALID_STATES:
            return jurisdiction
        else:
            logging.warning(f"Sorry, we currently only support filings for {', '.join(VALID_STATES)}. Please enter a valid state.")

# example / template lines of questioning

class BaseQuestion:
    def common_questions(self):
        # Code for questions that are common across all states
        pass

class CAQuestion(BaseQuestion):
    def state_specific_questions(self):
        # California specific questions
        pass

    def all_questions(self):
        self.common_questions()
        self.state_specific_questions()

class DEQuestion(BaseQuestion):
    def state_specific_questions(self):
        # Delaware specific questions
        pass

    def all_questions(self):
        self.common_questions()
        self.state_specific_questions()

def ask_yes_no_question(prompt):
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Invalid response. Please enter 'y' or 'n'.")




# questions.py
# Questions and State Form Handling

# Imports
import json
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

from classes.BaseForm.base_form import BaseForm
form_instance = BaseForm()

from classes.Jurisdiction.jurisdiction import Jurisdiction
def load_json_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# JSON configuration function
config = load_json_config("config.json")
form_config = load_json_config('field_coordinates.json')
VALID_STATES = config.get('VALID_STATES', [])
ENTITY_TYPES = config.get('ENTITY_TYPES', [])
FILING_TYPES = config.get('FILING_TYPES', [])
ALL_STATES = config.get('ALL STATES', [])
MAX_FORM_QUANTITY = config.get('MAX_FORM_QUANTITY', 10)
VALID_AGENT_NAMES = config.get('VALID_AGENT_NAMES', [])
DEFAULTS = config.get('DEFAULTS', [])

def get_confirmation(prompt):
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Invalid response. Please enter 'y' or 'n'.")

# functions moved in from main.py #

# Collect signer's name
def get_signer_name():
    signer_first = input("Enter the signer's first name: ")
    signer_mid = input("Enter the signer's middle name or initial, if any: ")
    signer_last = input("Enter the signer's last name: ")
    return f"{signer_first} {signer_mid} {signer_last}"

# Confirm filing type (currently COA only)
def confirm_filing_type():
    while True:
        filing_type = input(f"Note: FormWizard only supports form completion for 'Change of Agent' at this time. Please confirm (COA): ")
        if filing_type in FILING_TYPES:
            form_instance.filing_type = filing_type
            break
        else:
            logging.warning("Only Change of Agent filing type is currently supported.\n Please check back later for more filing types in the future or enter 'COA' to proceed.")

# Ask for number of forms to complete
def ask_total_forms():
    while True:
        try:
            num_forms = int(input("How many forms would you like to prepare for this session? (Up to 10): "))
            if 1 <= num_forms <= MAX_FORM_QUANTITY:
                break
            logging.warning(f"Please enter a number between 1 and {MAX_FORM_QUANTITY}.")
        except ValueError:
            logging.warning("Invalid input. Please enter a number.")
        return num_forms
# Confirm limited # of states are currently supported
def confirm_limited_states():
    while True:
        state_code = input("FormWizard currently supports filings for Delaware (DE) and California (CA) only. Please enter the corresponding state code (DE/CA): ").upper()
        if state_code in VALID_STATES:
            state_name = VALID_STATES[state_code]
            break
        logging.warning("Sorry, we currently only support filings for Delaware (DE) and California (CA). Please check back later for more states.")
            return state_code
# Confirm agent name
def confirm_agent_name():
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

# Confirm Signer's Name
def confirm_signer(signer_name):
    while True:
        signer_name = get_signer_name()
        if get_confirmation(f"Signer's full name is {signer_name}. Is this correct? (Y/N): "):
            logging.info(f"Signer's name confirmed as {signer_name}")
            break
        else:
            logging.warning("Signer's name not confirmed. Asking for re-entry.")

# Collect entity info
def get_entity_info(num_forms, ENTITY_TYPES):
    entities = []
    for i in range(num_forms):
        # Entity Name
        entity_name = input(f"Enter the full name of entity {i+1} of {num_forms}, including corporate indicator: ")
        while True:
            entity_type = input(f"Enter the entity type for {entity_name}: (LLC/Corp/LP): ")
            if entity_type in ENTITY_TYPES:
                break
            else:
                logging.warning("Invalid entity type, or type is not supported. Please select from the approved list (LLC/Corp/LP) again.")
        entities.append((entity_name, entity_type))
    return entities

# Domestic State
def get_domestic_state():
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

if __name__ == "__main__":
    main()





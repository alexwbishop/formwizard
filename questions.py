# questions.py
# Questions and State Form Handling

# Imports
import json
from responsibleparty import ResponsibleParty
from address import Address
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

from responsibleparty import ResponsibleParty
from address import Address
address_attributes = {
    "phys": ["phys_street1", "phys_city", "phys_state", "phys_zip"],
    "mail": ["mail_street1", "mail_city", "mail_state", "mail_zip"],
    "domestic": ["domestic_street1", "domestic_city", "domestic_zip", "domestic_county"]
}
responsible_party_attributes = {
    "officer1": ["officer1_first", "officer1_mid", "officer1_last", "officer1_street1", "officer1_city", "officer1_state", "officer1_zip"],
    "officer2": ["officer2_first", "officer2_mid", "officer2_last", "officer2_street1", "officer2_city", "officer2_state", "officer2_zip"],
    "officer3": ["officer3_first", "officer3_mid", "officer3_last", "officer3_street1", "officer3_city", "officer3_state", "officer3_zip"],
    "director1": ["director1_first", "director1_mid", "director1_last", "director1_street1", "director1_city", "director1_state", "director1_zip"],
    "agenthuman": ["agenthuman_first", "agenthuman_mid", "agenthuman_last", "agenthuman_street1", "agenthuman_city", "agenthuman_zip", "agenthuman_county"]
}
# set up address dictionary
address_attributes = {
    "phys": ["phys_street1", "phys_city", "phys_state", "phys_zip", "phys_county"],
    "mail": ["mail_street1", "mail_city", "mail_state", "mail_zip", "mail_county"],
    "domestic": ["domestic_street1", "domestic_city", "domestic_zip", domestic_county"]
}
responsible_party_attributes = {
    "officer1": ["officer1_first", "officer1_mid", "officer1_last", "officer1_street1", "officer1_city", "officer1_state", "officer1_zip"],
    "officer2": ["officer2_first", "officer2_mid", "officer2_last", "officer2_street1", "officer2_city", "officer2_state", "officer2_zip"],
    "officer3": ["officer3_first", "officer3_mid", "officer3_last", "officer3_street1", "officer3_city", "officer3_state", "officer3_zip"],
    "director1": ["director1_first", "director1_mid", "director1_last", "director1_street1", "director1_city", "director1_state", "director1_zip"],
    "agenthuman": ["agenthuman_first", "agenthuman_mid", "agenthuman_last", "agenthuman_street1", "agenthuman_city", "agenthuman_zip", "agenthuman_county"]
}

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
# Modify the get_jurisdiction function to accept entity_name as a parameter
def get_jurisdiction(entity_name: str) -> str:
    while True:
        jurisdiction = input(f"Enter the state that {entity_name} will file in (i.e. DE, CA): ").upper()
        if jurisdiction in VALID_STATES:
            return jurisdiction
        else:
            logging.warning(f"Sorry, we currently only support filings for {', '.join(VALID_STATES)}. Please enter a valid state.")

# Modify the main function to retrieve entity_name and pass it to get_jurisdiction
def main():
    # Assuming the first entity for simplicity; you can modify this based on your requirements
    entity_name = entities[0][0]  
    jurisdiction = get_jurisdiction(entity_name)

# NEW line of questioning
class BaseQuestion:
    def common_questions(self):
        # Common questions for all states
        self.signer_name = get_signer_name()
        self.filing_type = confirm_filing_type()
        self.num_forms = ask_total_forms()
        self.entities = get_entity_info(self.num_forms, ENTITY_TYPES)
        self.domestic_state = get_domestic_state()
        self.jurisdiction = get_jurisdiction(self.entity_name)

class CAQuestion(BaseQuestion):
    def state_specific_questions(self):
    # California specific questions #
        import re
from datetime import date

class FormWizard:
    def __init__(self):
        self.ca_entity_name = input("What is the entity name?")
        
        # Ensure state_id is numeric and up to 15 characters
        while True:
            self.ca_state_id = input("What is the state ID (numeric up to 15 characters)?")
            if self.ca_state_id.isdigit() and len(self.ca_state_id) <= 15:
                break
            print("Invalid input. Please enter a numeric state ID up to 15 characters.")
        
        # Ensure domestic_state is 2 characters and valid
        valid_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
                        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
                        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
                        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
                        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC"]
        while True:
            self.ca_domestic_state = input("What is the domestic state (2 digit US state or DC)?").upper()
            if self.ca_domestic_state in valid_states:
                break
            print("Invalid input. Please enter a valid 2 digit US state or DC.")
        
        # Ensure business_purpose is under 50 characters
        while True:
            self.ca_business_purpose = input("What is the business purpose?")
            if len(self.ca_business_purpose) <= 50:
                break
            print("Invalid input. Business purpose must be under 50 characters.")
        
        self.ca_CAlabor_yes = input("Is CA labor compliance met? (yes/no)").lower() == "yes"
        self.ca_CAlabor_no = not self.ca_CAlabor_yes
        
        # Validate email format
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        while True:
            self.ca_company_email = input("What is the company email?")
            if re.match(email_pattern, self.ca_company_email):
                break
            print("Invalid input. Please enter a valid email format.")
        
        self.ca_signed_on_date = date.today().strftime('%Y-%m-%d')
        print(f"Signed on Date: {self.ca_signed_on_date}")
        
        self.ca_signer_name = input("What is the signer's first and last name?")
        
        # Ensure signer_title is alpha and up to 50 characters
        while True:
            self.ca_signer_title = input("What is the signer's title (alpha only up to 50 characters)?")
            if self.ca_signer_title.isalpha() and len(self.ca_signer_title) <= 50:
                break
            print("Invalid input. Signer title should be alpha only and up to 50 characters.")

#SCARLET - Help with building code for new CA prompts below #

# ask for principal business address #
    # ask if same as mailing, if any #
    # ask if same as local office in CA, if any
    # if no, prompt for mailing address
# ask for street address of local office in California
    # if no, proceed
    # if yes, prompt for in-state address
    # validate address

#SCARLET - prompt for 3 officers with specified titles: Chief Executive Officer, Secretary, Chief Financial Officer, and 1 Director. #
  
for obj_name, attributes in address_attributes.items():
    inputs = {attr: input(f"Enter {attr}: ") for attr in attributes}
    if "state" in attributes:
        address = Address(inputs[attributes[0]], inputs[attributes[1]], inputs[attributes[2]], inputs[attributes[3]])
    else:
        address = Address(inputs[attributes[0]], inputs[attributes[1]], None, inputs[attributes[2]])
    # Store address instances wherever required

for obj_name, attributes in responsible_party_attributes.items():
    inputs = {attr: input(f"Enter {attr}: ") for attr in attributes}
    address = Address(inputs[attributes[3]], inputs[attributes[4]], inputs[attributes[5]], inputs[attributes[6]])
    responsible_party = ResponsibleParty(inputs[attributes[0]], inputs[attributes[1]], inputs[attributes[2]], address)
    # Store responsible_party instances wherever required

#SCARLET -    
    # DOMESTIC ENTITY ONLY: number of vacancies on board of directors, if any
    # confirm CT is to be the agent
    # prompt for business purpose (50 chars)
    # ask labor judgement question (Y/N) - Default to N
    # optional email address entry - validate email
    # confirm if any of the newly added officers will sign this form
    # if no, default to default signer previously specified
    # questioning complete

# ask DE specific questions #
class DEQuestion(BaseQuestion):
    def state_specific_questions(self):
        # Add any DE-specific questions here
        pass
        
# ask standard questions for all entities
    def all_questions(self):
        self.common_questions()
        self.state_specific_questions()
        
# return to entering info for next entity in the list
def main():
    jurisdiction = get_jurisdiction(entity_name)
    if jurisdiction == "CA":
        question_obj = CAQuestion()
    elif jurisdiction == "DE":
        question_obj = DEQuestion()
    else:
        print("Unexpected jurisdiction value entered.")
        return
    question_obj.all_questions()

# closing
if __name__ == "__main__":
    main()





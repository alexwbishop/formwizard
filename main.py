# FormWizard by Alex Bishop - incyde@riseup.net
# Version 1.0.0.2
# Purpose: Automate the process of filling out Change of Agent forms (Corp, LLC, LP), Domestic and Foreign. in DE and CA.
# main.py

# Imports
import json
import os
import PyPDF2
import uuid
import logging

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from classes.BaseForm.base_form import BaseForm
from classes.Jurisdiction.jurisdiction import Jurisdiction

## Define all functions

# logging enabled
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='formwizard.log')

# date & time validation
from datetime import datetime
try:
    current_time = datetime.now()
    logging.info(f"Current time:", {current_time}")
except Exception as e:
    logging.error(f"An error occurred:", {e}")
    # Here you could also log the error or take corrective measures

# JSON configuration function
def load_json_config(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON configuration: {e}")
    except FileNotFoundError as e:
        logging.error(f"JSON file not found: {e}")
    return {}

# Load JSON configurations
config = load_json_config('config.json')
form_config = load_json_config('field_coordinates.json')

VALID_STATES = config.get('VALID_STATES', {})
ENTITY_TYPES = config.get('ENTITY_TYPES', [])
FILING_TYPES = config.get('FILING_TYPES', [])
MAX_FORM_QUANTITY = config.get('MAX_FORM_QUANTITY', 10)
VALID_AGENT_NAMES = config.get('VALID_AGENT_NAMES', [])

# Function to collect signer's name
def get_signer_name():
    signer_first = input("Enter the signer's first name: ")
    signer_mid = input("Enter the signer's middle name or initial, if any: ")
    signer_last = input("Enter the signer's last name: ")
    return f"{signer_first} {signer_mid} {signer_last}"

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

# Function to check if a file exists
def file_exists(filepath):
    try:
        return os.path.isfile(filepath)
    except Exception as e:
        logging.error(f"An error occurred:", {e}")
        return False

# Function to get PDF dimensions
def get_pdf_dimensions(pdf_path):
    try:
        pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
        page = pdf_reader.pages[0]  # Reads the first page
        media_box = page.mediabox
        return media_box.width, media_box.height  
    except Exception as e:
        logging.error(f"An error occurred while reading PDF", {e}")
        return None, None

# Function to populate form fields
def populate_form(form_template_path, output_pdf_path, field_coordinates, field_values):
    _, height = get_pdf_dimensions(form_template_path)
    c = canvas.Canvas(output_pdf_path)
    c.setFont("Helvetica", 12)

    for field, coordinates in field_coordinates.items():
        x = coordinates['x']
        y = height - coordinates['y']
        value = field_values.get(field, '')
        c.drawString(x, y, str(value))

    c.save()
    
# Function to merge text PDF onto blank form
from PyPDF2 import PdfReader, PdfWriter

# Define creation of session id#
def generate_session_id():
    session_id = uuid.uuid4().hex.upper()[0:6]
    return session_id

# Create a DE and CA instance of the Jurisdiction class
de_jurisdiction = Jurisdiction.create_jurisdiction("Delaware", "DE")
ca_jurisdiction = Jurisdiction.create_jurisdiction("California", "CA")

# BaseForm: Instantiate to begin storing the inputted data with some default settings
form_instance = BaseForm(
    domestic_state="DE", 
    form_status="Blank", 
    session_timestamp=datetime.now(), 
    signed_on_date=datetime.now(),
    jurisdiction_instance=de_jurisdiction,
)

# Now that form_instance is defined, you can update de_jurisdiction with it if needed
de_jurisdiction.jurisdiction_instance = form_instance

def merge_pdfs(form_pdf_path, text_pdf_path, output_pdf_path):
    pdf_reader_form = PdfReader(open(form_pdf_path, 'rb'))
    pdf_reader_text = PdfReader(open(text_pdf_path, 'rb'))
    
    pdf_writer = PdfWriter()
    
    page_form = pdf_reader_form.pages[0]
    page_text = pdf_reader_text.pages[0]
    
    page_form.merge_page(page_text)
    pdf_writer.add_page(page_form)
    
    with open(output_pdf_path, 'wb') as f:
        pdf_writer.write(f)

# Use the defaults
form_instance = BaseForm(
    domestic_state=DEFAULTS.get('domestic_state', 'DE'), 
    form_status=DEFAULTS.get('form_status', 'Blank'), 
    session_timestamp=datetime.now(), 
    signed_on_date=datetime.now(),
    jurisdiction_instance=de_jurisdiction,
)
## PHASE 1 = Basic command line prompt usage:

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
if __name__ == "__main__":
    session_id = generate_session_id()
#  assign the user_id and timestamp to the session markers
form_instance.user_id = user_id
form_instance.session_id = session_id
form_instance.session_timestamp = datetime.now()
logging.info(f"Thank you for authenticating, {user_id}! \n Form prep session initialized. \n Username: {user.id} | Session ID: {session_id}") | Timestamp: {session_timestamp}")

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

# Create an instance of the Jurisdiction class based on user input
jurisdiction_instance = Jurisdiction.create_jurisdiction(state_name, state_code)

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

# Initialize list to store form instances
forms = []

# Load applicable jurisdiction names and abbreviations for the form-prep session
## redundant? # de_jurisdiction = Jurisdiction("Delaware", "DE")
## redundant? # ca_jurisdiction = Jurisdiction("California", "CA")

# Store inputted signature block info into previously initialized BaseForm instance
form_instance.agent_name = agent_name
form_instance.signer_first = signer_first
form_instance.signer_mid = signer_mid
form_instance.signer_last = signer_last
form_instance.signer_name = signer_name
form_instance.sig_conformed = sig_conformed
form_instance.sig_typed = signer_name

## Collect entity info

# Initialize a list to store entity data
entity_data_list = []

# Loop to collect entity info
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
    
    # Residency
    residency = 'Dom' if jurisdiction == domestic_state else 'For'

    # Store entity data in a dictionary
    entity_data = {
        'entity_name': entity_name,
        'entity_type': entity_type,
        'domestic_state': domestic_state,
        'jurisdiction': jurisdiction,
        'residency': residency
    }
    
    # Add to list
    entity_data_list.append(entity_data)
    
# Entity Info Confirmation
def collect_entity_info():
    while True:
        entity_name, domestic_state, entity_type, filing_type, agent_name, jurisdiction = gather_entity_details()
        if get_confirmation(f"Entity info entered: {entity_name} (a {domestic_state} {entity_type}) is filing a {filing_type} to {agent_name} in {jurisdiction}. Is this correct? (Y/N): "):
            return entity_name, domestic_state, entity_type, filing_type, agent_name, jurisdiction
        else:
            logging.warning("Please re-enter the entity details.")

# Print all collected entity data for confirmation
for i, data in enumerate(entity_data_list):
    logging.info(f"Entity {i+1}: {data['entity_name']} (a {data['domestic_state']} {data['entity_type']},)
           is filing a {data['residency']} {data['filing_type']} in {data['jurisdiction']}.")

# Store each set of inputted entity data from the list (up to 10) into the previously initialized BaseForm instance:
    form_instance.signer_first = signer_first
    form_instance.signer_mid = signer_mid
    form_instance.signer_last = signer_last
    form_instance.signer_name = f"{signer_first} {signer_mid} {signer_last}"

# Construct the PDF file path dynamically
form_template_path = f"StateForms/{jurisdiction}/{jurisdiction}-{entity_type}-{residency}-{filing_type}.pdf"

# Check if PDF files exist
def check_file_path():
    while True:
        if file_exists(form_template_path):
            return form_template_path
        else:
            logging.warning(f"Error: The template PDF file, {form_template_path}, is missing.")
            custom_path = input("Would you like to provide a custom path for the template PDF file? (Y/N): ").lower()
            if custom_path == 'y':
                form_template_path = input("Please enter the custom path: ")
            else:
                logging.warning("Please place the template PDF file in the correct location and restart.")

# store the data into the form class
form_instance.entity_name = entity_name,
form_instance.entity_type = entity_type,
form_instance.jurisdiction_instance = None,  # Not yet used - to pull attributes from jurisdiction class
form_instance.domestic_state = domestic_state,
form_instance.residency = residency,
form_instance.filing_type = filing_type,

forms.append(form_instance)

# It should loop through the total # of filings requested (up to 10) and store each data set into 'forms', then display below

# Display a complete list of up to 10 entities & forms to be filled
logging.info(f"List of entities/forms to be filled in this session: ")
for i, form in enumerate(forms):
    logging.info(f"{i+1}) form.entity_name - form.entity_type - form.filing_type")

# Ask user to confirm the list of filings Y/N to proceed. If N, go back.
def prepare_filings():
    while True:
        num_forms, form_list = gather_filing_details()
        if get_confirmation(f"All information for form preparation request has been obtained, we are ready to complete {num_forms} forms now. Proceed? (Y/N): "):
            return num_forms, form_list
        else:
            logging.warning("Please restart the session with the correct information.")

# ZIP code validation (not yet being used)
#agent_zip = input("Enter the agent's ZIP code: ")
#while not agent_zip.isdigit() or len(agent_zip) != 5:
#    agent_zip = input("Enter a valid ZIP code: ")

## PHASE 2 = DOCUMENT PREPARATION

# Update form_data with user input
form_data = {
    'entity_name': entity_name,
    'agent_name': agent_name,
    'sig_conformed': sig_conformed,
    'signer_name': signer_name
# Need to add functionality to load the registered agent address in from a separate library, based on selecting CT or NRAI as the agent_name
}

# define the form key for labeling PDF files being processed, e.g. DE-Corp-Dom-COA
form_key = f"{jurisdiction}-{entity_type}-{residency}-{filing_type}"

# Run the populate function on the form
populate_form(f'StateForms/{jurisdiction}/{form_key}.pdf', f'StateForms/{jurisdiction}/output_{form_key}.pdf', form_config.get(form_key, {}), form_data)

# Temporary text PDF path
temp_text_pdf_path = f'completed_forms/temp/temp_text_{form_key}.pdf'

# Populate form with text
populate_form(f'StateForms/{jurisdiction}/{form_key}.pdf', temp_text_pdf_path, form_config.get(form_key, {}), form_data)

# Merge the original form and text PDF
merge_pdfs(f'StateForms/{jurisdiction}/{form_key}.pdf', temp_text_pdf_path, f'completed_forms/{jurisdiction}-{entity_name}_-_{form_key}_Filled.pdf')

# Print all collected entity data for confirmation
for i, data in enumerate(entity_data_list):
    logging.info(f"PDF for: {data['entity_name']} - {data['jurisdiction']} {data['residency']} 
          {data['entity_type']},) {data['filing_type']}.")

# Show success message & goodbye
logging.info(f"Total PDFs filled: {num_forms}. Total errors: 0 \n Successfully completed session.  \n Thank you for using FormWizard!
\n Your session ID is: {session_id}. \n Time Completed: {session_timestamp} \n Have a great day, {user_id}!")

# prompt for text file export function

# prompt for feedback of experience 1-10

# Done! For now...

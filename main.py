# FormWizard by Alex Bishop - incyde@riseup.net
# Version 1.0.0.2
# Purpose: Automate the process of filling out Delaware Change of Agent forms (Corp, LLC, LP), Domestic and Foreign.

# main.py
# Imports
import json
import os
import PyPDF2
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from classes.BaseForm.base_form import BaseForm
from classes.Jurisdiction.jurisdiction import Jurisdiction

## Define all functions
# Function to check if a file exists
def file_exists(filepath):
    return os.path.isfile(filepath)

# Function to get PDF dimensions
def get_pdf_dimensions(pdf_path):
    pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    page = pdf_reader.pages[0]  # Reads the first page
    media_box = page.mediabox
    return media_box.width, media_box.height  

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

# Create a DE instance of the Jurisdiction class
de_jurisdiction = Jurisdiction.create_jurisdiction("Delaware", "DE")

# BaseForm: Instantiate to begin storing the inputted data with some default settings
form_instance = BaseForm(
    domestic_state="DE", 
    form_status="Blank", 
    session_timestamp=datetime.now(), 
    signed_on_date=datetime.now(),
    jurisdiction_instance=de_jurisdiction  
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
    
# Load JSON configuration
with open('field_coordinates.json', 'r') as f:
    form_config = json.load(f)

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
#        print("Invalid format. Please enter a username in the correct format.")

# Ask for password
#password = input("Please enter your password: ")

# Check if the username and password are correct
#if user_id == 'alexander.bishop' and password == 'scarlet':
#    print("Welcome, Alex!")
#else:
#    print("Access denied. Please check your username and password.")
#    exit()

# Create a session_id for the form prep session and assign the user_id to it
session_id = "FW-Test-001"
form_instance.user_id = user_id
form_instance.session_id = session_id # make this dynamically-generated for each form-prep session (aka each successful run of program)
form_instance.session_timestamp = datetime.now()

# Confirm filing type
confirmation = input("FormWizard only supports form completion for Change of Agents at this time. Please confirm (Y/N): ").lower()
if confirmation != 'y':
    print("Please check back later for more filing types to be supported in the future.")
    exit()
filing_type = "COA"
form_instance.filing_type = filing_type

# Ask for number of forms to complete
num_forms = int(input("How many forms would you like to prepare for this session? (Up to 10): "))
if num_forms > 10:
    print("Sorry, you can only prepare up to 10 forms at a time.")
    exit()
if num_forms < 1:
    print("That's not even a real number. Why are you even here? Goodbye, silly person.")
    exit()

# Confirm state of filing (currently only DE or CA)
state_confirmation = input("FormWizard currently supports filings for Delaware (DE) and California (CA) only. Please enter the state code (DE/CA): ").upper()
if state_confirmation not in ['DE', 'CA']:
    print("Sorry, we currently only support filings for Delaware and California. Please check back later for more states.")
    exit()

# User selects the state based on input
state_name = "Delaware" if state_confirmation == 'DE' else "California"
state_code = state_confirmation

# Create an instance of the Jurisdiction class based on user input
jurisdiction_instance = Jurisdiction.create_jurisdiction(state_name, state_code)

# Ask if we are to use CT as Agent - Need to add validation to confirm if matched within agent name list or a custom name
agent_name = "C T Corporation System"
print(f"Please confirm that agent to be designated is: {agent_name} (Y/N): ")
confirmation = input().lower()
if confirmation != 'y':
    print("We can only change agents to CT at this time. Please check back later.")
    exit()
    
# Collect Signer's Name
signer_first = input("Enter the signer's first name: ")
signer_mid = input("Enter the signer's middle name or initial, if any: ")
signer_last = input("Enter the signer's last name: ")
signer_name = f"{signer_first} {signer_mid} {signer_last}"
sig_conformed = f"/s/{signer_name}"

 # Confirm Signer's Name
print(f"Signer's full name is {signer_name}. Is this correct? (Y/N): ")
confirmation = input().lower()
if confirmation != 'y':
    print("Please restart the session with the correct signer's name.")
    exit()

# Initialize list to store form instances
forms = []

# Load applicable jurisdiction names and abbreviations for the form-prep session
de_jurisdiction = Jurisdiction("Delaware", "DE")

# Store inputted signature block info into previously initialized BaseForm instance
form_instance.agent_name = agent_name
form_instance.signer_first = signer_first
form_instance.signer_mid = signer_mid
form_instance.signer_last = signer_last
form_instance.signer_name = signer_name
form_instance.sig_conformed = sig_conformed
form_instance.sig_typed = signer_first

# Collect entity info
for i in range(num_forms):
    entity_name = input(f"Enter the full name of entity {i+1} of {num_forms}, including corporate suffix: ")
    # need action to attempt to guess at the entity_type by scanning through the entity_name
    entity_type = input(f"Confirm the entity type for {entity_name} (LLC/Corp/LP): ")
    # need action to only allow those options to be selected
    domestic_state = input(f"Enter the domestic state/home jurisdiction of {entity_name} (i.e. DE): ")
    # need action to check if it's a valid state abbreviation
    jurisdiction = input(f"Enter the state to file {filing_type} for {entity_name} in (DE/CA): ")
    # need action to check if it's a jurisdiction that FormWizard can handle (DE or CA right now)
    residency = input(f"Is {entity_name} Domestic or Foreign to {jurisdiction}? (Dom/For): ")
    # need action for the above line to convert the response into a value for residency, as either domestic or foreign in relation to the jurisdiction variable.
    #filing_type = input(f"Is {entity_name} filing a Change of Agent in {jurisdiction}? (Y/N): ")
    # need action to set filing_type to be 'Change of Agent' if Y is selected, otherwise go back to last menu (because we can only handle 1 filing_type right now).
    break

# Confirm entered entity info before proceeding to next entity
confirmation_message = f"Entity info entered: {entity_name} (a {domestic_state} {entity_type}) is filing a {filing_type} in {jurisdiction}. Is this correct? (Y/N): "
print(confirmation_message)
confirmation = input().lower()
if confirmation != 'y':
    print("Please restart the session with the correct information.") # Need this to just go back a step to Collect entity names
    exit()
if confirmation != 'y':

# Store each set of inputted entity data from the list (up to 10) into the previously initialized BaseForm instance:
    form_instance.signer_first = signer_first
    form_instance.signer_mid = signer_mid
    form_instance.signer_last = signer_last
    form_instance.signer_name = f"{signer_first} {signer_mid} {signer_last}"

# Construct the PDF file path dynamically
form_template_path = f"StateForms/{jurisdiction}/{jurisdiction}-{entity_type}-{residency}-{filing_type}.pdf"

# Check if PDF files exist
if not file_exists(form_template_path):
    print(f"Error: The template PDF file, {form_template_path}, is missing.")
    exit(1)

# store the data into the form class
form_instance.entity_name = entity_name,
form_instance.entity_type = entity_type,
form_instance.jurisdiction_instance = None,  # Not yet used - to pull attributes from jurisdiction class
form_instance.domestic_state = domestic_state,
form_instance.residency = residency,
form_instance.filing_type = filing_type,

forms.append(form_instance)

# It should loop through the total # of filings requested (up to 10) and store each data set into 'forms'

# Display complete list of entities & forms to be filled
print("List of entities/forms to be filled in this session:")
for i, form in enumerate(forms):
    print(f"{i+1}) form.entity_name - form.entity_type - form.filing_type")

# Ask user to confirm the list of filings Y/N to proceed. If N, quit program.
print(f"All information obtained, ready to complete forms now. Proceed? (Y/N): ")
confirmation = input().lower()
if confirmation != 'y':
    print("Please restart the session with the correct information.")
    exit()

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

# define the form key for labeling PDF files being processed, e.g. DE-Corp-For-COA
form_key = f"{jurisdiction}-{entity_type}-{residency}-{filing_type}"

# Run the populate function on the form
populate_form(f'StateForms/{jurisdiction}/{form_key}.pdf', f'StateForms/{jurisdiction}/output_{form_key}.pdf', form_config.get(form_key, {}), form_data)

# Temporary text PDF path
temp_text_pdf_path = f'completed_forms/temp/temp_text_{form_key}.pdf'

# Populate form with text
populate_form(f'StateForms/{jurisdiction}/{form_key}.pdf', temp_text_pdf_path, form_config.get(form_key, {}), form_data)

# Merge the original form and text PDF
merge_pdfs(f'StateForms/{jurisdiction}/{form_key}.pdf', temp_text_pdf_path, f'completed_forms/{jurisdiction}-{entity_name}_-_{form_key}_Filled.pdf')

# Show success message
print(f"PDF for {entity_name} Successfully Filled. Thank you for using FormWizard. Your session ID is: {session_id}.")

# Done! For now...
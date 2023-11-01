# FormWizard by Alex Bishop - incyde@riseup.net
# Version 1.0.0.2
# Purpose: Automate the process of filling out Delaware Change of Agent forms (Corp, LLC, LP), Domestic and Foreign.

## Import stuff
# Imports
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import json
import os

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

# Initialize an empty BaseForm instance to begin storing the inputted data
form_instance = BaseForm()

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

# PHASE 1 = Basic command line prompt usage:

# Greet and Confirm that User is Alex
user_id = input("Hello! Are you Alex? (Y/N): ")
# Develop this further to ask for the WK username and validate correct format before asking for password. Once validated, store the WK username as user_id variable.
if user_name.lower() == 'y':
    password = input("Please enter your password: ")
    if password == 'scarletrules':
        print("Welcome, Alex!")
# add deeper password security here
    else:
        print("Incorrect password. Exiting.")
        exit()
else:
    print("You are not authorized to use this program. Exiting.")
    exit()
    
# Store the user_id into the session
form_instance.user_id = {user_id}
form_instance.session_id = {session_id}
form_instance.session_timestamp = {}

# Ask for number of forms to complete
num_forms = int(input("How many DE forms would you like to prepare for this session? (Up to 10): "))
if num_forms > 10:
    print("Sorry, you can only prepare up to 10 forms at a time.")
    exit()

# Ask if we are to use CT or NRAI as Agent
    agent_name = input(f"Confirm the agent to be designated: (CT/NRAI)")
    
# Collect Signer's Name
    signer_first = input("Enter the signer's first name: ")
    signer_mid = input("Enter the signer's last name: ")
    signer_last = input("Enter the signer's last name: ")
    
 # Confirm Signer's Name
print(f"Signer's full name is {signer_first} {signer_mid} {signer_last}. Is this correct? (Y/N): ")
confirmation = input()
if confirmation.lower() != 'y':
    print("Please restart the session with the correct signer's name.")
    exit()

# Initialize list to store form instances
forms = []

# Store inputted signature block info into previously initialized BaseForm instance
form_instance.agent_name = {agent_name}
form_instance.signer_first = {signer_first}
form_instance.signer_mid = {signer_mid}
form_instance.signer_last = {signer_last}
form_instance.signer_name = {signer_first} {signer_mid} {signer_last}
form_instance.sig_conformed = f"/s/{signer_name}"
form_instance.sig_typed = {signer_first}


# Collect entity names, types, and residency
for i in range(num_forms):
    entity_name = input(f"Enter the full name of entity {i+1} of range(num_forms), including corporate suffix: ")
    # need action to attempt to guess at the entity_type by scanning through the entity_name
    entity_type = input(f"Confirm the entity type for {entity_name} (LLC/Corp/LP): ")
    # need action to only allow those options to be selected
    domestic_state = input(f"Enter the domestic state/home jurisdiction of {entity_name} (i.e. DE): ")
    # need action to check if it's a valid state abbreviation
    jurisdiction = input(f"Enter the state to file {filing_type} for {entity_name} in (DE/CA): ")
    # need action to check if it's a jurisdiction that FormWizard can handle (DE or CA right now)
    residency = input(f"Is {entity_name} Domestic or Foreign to {jurisdiction}? (D/F): ")
    # need action for the above line to convert the response into a value for residency, as either domestic or foreign in relation to the jurisdiction variable.
    filing_type = input(f"Is {entity_name} filing a Change of Agent in {jurisdiction}? (Y/N): ")
    # need action to set filing_type to be 'Change of Agent' if Y is selected, otherwise go back to last menu (because we can only handle 1 filing_type right now).
    
    print(f"Entity info entered: {entity_name} (a {residency} {entity_type}) is filing a {filing type} in {jurisdiction}. Is this correct? (Y/N): ")
        confirmation = input()
        if confirmation.lower() == 'y':
            break

# Store each set of inputted entity data from the list (up to 10) into the previously initialized BaseForm instance:
form_instance.signer_first = {signer_first}
form_instance.signer_mid = {signer_mid}
form_instance.signer_last = {signer_last}
form_instance.signer_name = {signer_first} {signer_mid} {signer_last}
form_instance.sig_conformed = f"/s/ {signer_first}"

# Construct the PDF file path dynamically
form_template_path = f"StateForms/{form_instance.jurisdiction}/{form_instance.jurisdiction}-{form_instance.entity_type}-{form_instance.residency}-{form_instance.filing_type}.pdf

# Check if PDF files exist
if not file_exists(form_template_path):
    print(f"Error: The template PDF file, {pdf_file_path}, is missing.")
    exit(1)

# store the data into the form class
form_instance.entity_name=entity_name,
form_instance.entity_type=entity_type,
form_instance.jurisdiction_instance=None,  # Not yet used - to pull attributes from jurisdiction class
form_instance.domestic_state=domestic_state,
form_instance.residency=residency,
form_instance.filing_type=filing_type,
)

forms.append(form_instance)

# It should loop through the total # of filings requested (up to 10) and store each data set into 'forms'

# Display complete list of entities & forms to be filled
print("List of entities/forms to be filled in this session:")
for i, form in enumerate(forms):
    print(f"{i+1}) {form.entity_name} - {form.entity_type} - {form.filing_type}")

# Ask user to confirm the list of filings Y/N to proceed. If N, quit program.
print(f"All information obtained, ready to complete forms now. Proceed? (Y/N): ")
confirmation = input()
if confirmation.lower() != 'y':
    print("Please restart the session with the correct information.")
    exit()

# ZIP code validation (not yet being used)
agent_zip = input("Enter the agent's ZIP code: ")
while not agent_zip.isdigit() or len(agent_zip) != 5:
    agent_zip = input("Enter a valid ZIP code: ")

# Update form_data with user input
form_data = {
    'entity_name': entity_name,
    'agent_name': agent_name,
    'sig_conformed': sig_conformed,
    'signer_name': signer_name
# Need to add functionality to load the registered agent address in from a separate library, based on selecting CT or NRAI as the agent_name
}

# Run the populate function on the form
populate_form(f'StateForms/{jurisdiction}/{form_key}.pdf', f'StateForms/{jurisdiction}/output_{form_key}.pdf', form_config.get(form_key, {}), form_data)

# Temporary text PDF path
temp_text_pdf_path = f'completed_forms/temp/temp_text_{form_key}.pdf'

# Populate form with text
populate_form(f'StateForms/{jurisdiction}/{form_key}.pdf', temp_text_pdf_path, form_config.get(form_key, {}), form_data)

# Merge the original form and text PDF
merge_pdfs(f'StateForms/{jurisdiction}/{form_key}.pdf', temp_text_pdf_path, f'completed_forms/{jurisdiction}-{entity_name}_-_{form_key}_Filled.pdf')

# Show success message
print(f"PDF for {entity_name} Successfully Filled.")

# Done! For now...

# FormWizard by Alex Bishop - incyde@riseup.net
# Version 1.0.0.2
# Purpose: Automate the process of filling out Delaware Change of Agent forms (Corp, LLC, LP), Domestic and Foreign.

## Import stuff
# Imports
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
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

# Assume base_filepath is an instance of BaseForm
#SCARLET: Is this redundant? jurisdiction = base_filepath_instance.jurisdiction
#SCARLET: Is this redundant? entity_type = base_filepath_instance.entity_type
#SCARLET: Is this redundant? residency = base_filepath_instance.residency
#SCARLET: Is this redundant? filing_type = base_filepath_instance.filing_type

# Construct the PDF file path dynamically
form_template_path = f"StateForms/{jurisdiction}/{jurisdiction}-{entity_type}-{residency}-{filing_type}.pdf"

# Function to merge text PDF onto blank form
from PyPDF2 import PdfReader, PdfWriter

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



# Check if PDF files exist
if not file_exists("form_template_path"):
    print("Error: The template PDF file {pdf_file_path} is missing.")
    exit(1)
    
# Load JSON configuration
with open('field_coordinates.json', 'r') as f:
    form_config = json.load(f)

# PHASE 1 = Basic command line prompt usage:

# Greet and Confirm that User is Alex
user_name = input("Hello! Are you Alex? (Y/N): ")
if user_name.lower() == 'y':
    password = input("Please enter your password: ")
    if password == 'scarletrules':
        print("Welcome, Alex!")
    else:
        print("Incorrect password. Exiting.")
        exit()
else:
    print("You are not authorized to use this program. Exiting.")
    exit()

# Ask for number of forms to complete
num_forms = int(input("How many DE forms would you like to prepare for this session? (Up to 10): "))
if num_forms > 10:
    print("Sorry, you can only prepare up to 10 forms at a time.")
    exit()

# Ask if we are to use CT or NRAI as Agent
    agent_name = input(f"Confirm the agent to be designated: ")
    
# Collect Signer's Name
    signer_first_name = input("Enter the signer's first name: ")
    signer_last_name = input("Enter the signer's last name: ")
    
 # Confirm Signer's Name
print(f"Signer's full name is {signer_first_name} {signer_last_name}. Is this correct? (Y/N): ")
confirmation = input()
if confirmation.lower() != 'y':
    print("Please restart the session with the correct signer's name.")
    exit()

# Initialize list to store form instances
forms = []

# Collect entity names, types, and residency
for i in range(num_forms):
    entity_name = input(f"Enter the name of entity {i+1}: ")
    entity_type = input(f"Confirm the entity type for {entity_name} (LLC/Corp/LP): ")
    dom_for = input(f"Is {entity_name} Domestic or Foreign to Delaware? (Y/N): ")

# Validate inputs (example for ZIP code)
while not agent_zip.isdigit() or len(agent_zip) != 5:
        agent_zip = input("Enter a valid ZIP code: ")
    
    print(f"Entity info entered: {entity_name} - {entity_type} ({dom_for}). Is this correct? (Y/N): ")
        confirmation = input()
        if confirmation.lower() == 'y':
            break

# Create an instance of your form class and store the data
form_instance = BaseForm(
    entity_name=entity_name,
    jurisdiction_instance=None,  # You'll need to set this
    domestic_state=dom_for,
    agent_name=agent_name,
    agent_street1=None,  # You'll need to set this
    # ... (and so on for all the other attributes)
    user_id="Alex"  # Since you're the user
)

forms.append(form_instance)

# Display list of entities & forms to be filled
print("List of entities/forms to be filled in this session:")
for i, form in enumerate(forms):
    print(f"{i+1}) {form.entity_name} - {form.entity_type} - Filing Type (Change of Agent)")

# Display signer's conformed signature
conformed_signature = f"/s/{signer_first_name} {signer_last_name}"
print(f"Conformed signature: {conformed_signature}")

# Ask user to confirm Y/N to proceed. If N, quit program.
print(f"All information obtained, ready to complete forms now. Proceed? (Y/N): ")
confirmation = input()
if confirmation.lower() != 'y':
    print("Please restart the session with the correct information.")
    exit()


# Update form_data with user input
form_data = {
    'entity_name': entity_name,
    'agent_name': agent_name,
    'sig_conformed': sig_conformed,
    'signer_name': signer_name
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

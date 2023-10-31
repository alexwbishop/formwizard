# FormWizard by Alex Bishop - incyde@riseup.net
# Version 1.0.0.2
# Purpose: Automate the process of filling out Delaware Change of Agent forms (Corp, LLC, LP), Domestic and Foreign.

# Import stuff
import json
from reportlab.pdfgen import canvas
import PyPDF2

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

# Load JSON configuration
with open('field_coordinates.json', 'r') as f:
    form_config = json.load(f)

# PHASE 1 = Basic command line prompt usage:

# Function to get user input for form type and details
def get_user_input():
    print("Select the entity type:")
    entity_type = input("1: LLC\n2: Corp\n3: LP\n")
    
    print("Select Domestic or Foreign:")
    dom_for = input("1: Domestic\n2: Foreign\n")
    
    print("Confirm the agent:")
    agent_choice = input("1: CT (The Corporation Trust Company)\n2: NRAI (National Registered Agents, Inc.)\n")
    
    # Map user input to actual values
    entity_map = {'1': 'LLC', '2': 'Corp', '3': 'LP'}
    dom_for_map = {'1': 'Dom', '2': 'For'}
    agent_map = {'1': 'The Corporation Trust Company', '2': 'National Registered Agents, Inc.'}
    
    entity_type = entity_map.get(entity_type, 'LLC')
    dom_for = dom_for_map.get(dom_for, 'Dom')
    agent_name = agent_map.get(agent_choice, 'The Corporation Trust Company')
    
    return entity_type, dom_for, agent_name

# Get user input
entity_type, dom_for, agent_name = get_user_input()

# Construct form key based on user input (e.g., 'DE-LLC-Dom-COA')
form_key = f"DE-{entity_type}-{dom_for}-COA"

# Prompt user for remaining information
entity_name = input("Enter the entity name: ")
sig_conformed = input("Enter the conformed signature: ")
signer_name = input("Enter the signer's name: ")

# Update form_data with user input
form_data = {
    'entity_name': entity_name,
    'agent_name': agent_name,
    'sig_conformed': sig_conformed,
    'signer_name': signer_name
}

# Run the populate function on the form
populate_form(f'StateForms/DE/{form_key}.pdf', f'StateForms/DE/output_{form_key}.pdf', form_config.get(form_key, {}), form_data)

# Done! For now...
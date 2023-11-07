# FormWizard by Alex Bishop - incyde@riseup.net
# Version 1.0.0.2
# Purpose: 1) Data Extraction: Write a script to prompt for the required fields to be inserted into any Delaware Change of Agent form (Corp, LLC, LP).
#          2) PDF Manipulation: Write a script to take the extracted data and insert it into the PDF form at the correct coordinates.
#          3) PDF Saving: Saves each completed PDF into the root folder with the format: STATE- Entity Name-Dom/For-FormType-EntityName (e.g. "DE-LLC-Dom-Formation-ABC123 LLC.pdf")
# Let's import some stuff
import PyPDF2
import json
from reportlab.pdfgen import canvas

# Function to get PDF dimensions
def get_pdf_dimensions(pdf_path):
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_path, 'rb'))
    page = pdf_reader.getPage(0)  # Reads the first page
    media_box = page.mediaBox
    return media_box.getWidth(), media_box.getHeight()

# Function to populate form fields
def populate_form(form_template_path, output_pdf_path, field_coordinates, field_values):
    # Get the dimensions of the PDF
    _, height = get_pdf_dimensions(form_template_path)

    c = canvas.Canvas(output_pdf_path)
    c.setFont("Helvetica", 12)

 # Master address logic
    master_address = form_data.get('master_address', {})

    for field, coordinates in field_coordinates.items():
        x = coordinates['x']
        y = height - coordinates['y']  # Adjusting the y-coordinate based on the PDF height
        value = field_values.get(field, '')  # Fetch the value for this field from field_values dictionary
        c.drawString(x, y, str(value))

    c.save()

# Load JSON configuration
with open('field_coordinates.json', 'r') as f:
    form_config = json.load(f)
   
# Sample usage
form_data = {
    'entity_name': 'My Entity',
    'agent_name': 'Agent Smith',
    'sig_conformed': 'Conformed Signature',
    'signer_name': 'John Doe',
    'master_address': {
        'agent_street1': '123 Main St',
        'agent_city': 'Anytown',
        'agent_zip': '12345'
    }
}

# run the populate function on the form
populate_form('path/to/DE-LLC-Dom-COA.pdf', 'path/to/output.pdf', form_config.get('DE-LLC-Dom-COA', {}), form_data)


# Prompt user for required information
#
#?

# Now you have all the form data in variables, ready to be inserted into the PDF in the next step.

# load reportlab features
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

# load pyPDF2 features
from PyPDF2 import PdfReader, PdfWriter

# Read the original PDF
pdf_reader = PdfReader("LLCAmendCOA.pdf")

# Create a new PdfWriter object
pdf_writer = PdfWriter()

# Create the overlay PDF (containing customer data)
c = canvas.Canvas("LLCAmendCOA-Overlay.pdf", pagesize=letter)  # Changed pagesize to 'letter'
width, height = letter

# Add entity name
c.drawString(100, height - 225, f"{entity_name}")

# Add agent street address
c.drawString(150, height - 263, f"{agent_street_address}")

# Add agent city
c.drawString(350, height - 280, f"{agent_city}")

# Add agent zip
c.drawString(140, height - 295, f"{agent_zip}")

# Add name of agent
c.drawString(100, height - 320, f"{name_of_agent}")

# Add signer's name and title
c.drawString(320, height - 460, f"{signer_name}, {signer_title}")

# Add conformed signature
c.drawString(320, height - 520, f"{conformed_signature}")

# Save PDF
c.save()

# Add pages from the original PDF to the writer object
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]

    # Read the overlay PDF
    overlay_reader = PdfReader("LLCAmendCOA-Overlay.pdf")
    overlay_page = overlay_reader.pages[0]

    # Merge the overlay page onto the original page
    page.merge_page(overlay_page)

    # Add the merged page to the writer object
    pdf_writer.add_page(page)

# Write the changes to a new PDF
with open("LLCAmendCOA-Completed.pdf", "wb") as f_out:
    pdf_writer.write(f_out)

# Show success message
print("PDF for " + entity_name + " Successfully Filled.")

# Done!
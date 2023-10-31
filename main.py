
# FormWizard by Alex Bishop - incyde@riseup.net
# Version 1.0.0.2
# Purpose: 1) Data Extraction: Write a small script to prompt for the required fields to be inserted into any Delaware form.
#          2) PDF Manipulation: Write a script to take the extracted data and insert it into the PDF form at the correct coordinates.
#          3) PDF Saving: Saves each completed PDF into the root folder with the format: STATE- Entity Name - Dom/Foreign FormType i.e. "DE- LLC Dom Formation"

# Prompt user for required information
entity_name = input("Enter the entity name: ")
agent_street_address = input("Enter the agent's street address: ")
agent_city = input("Enter the agent's city: ")
agent_zip = input("Enter the agent's zip code: ")
name_of_agent = input("Enter the name of the agent: ")
signer_name = input("Enter the signer's name: ")
signer_title = input("Enter the signer's title: ")
conformed_signature = "/s/" + signer_name

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
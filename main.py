
# FormWizard by Alex Bishop - incyde@riseup.net
# Version 0.0.0.1
# Purpose: 1) Data Extraction: Write a small script to prompt for the required fields to be inserted into a DE domestic Change of Agent form.
#          2) PDF Manipulation: Write a script to take the extracted data and insert it into the PDF form at the correct coordinates.

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

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

# Create a blank PDF
c = canvas.Canvas("filled_form.pdf", pagesize=letter)
width, height = letter

# Add entity name
c.drawString(100, height - 100, f"Entity Name: {entity_name}")

# Add agent street address
c.drawString(100, height - 150, f"Agent Street Address: {agent_street_address}")

# Add agent city
c.drawString(100, height - 200, f"Agent City: {agent_city}")

# Add agent zip
c.drawString(100, height - 250, f"Agent Zip: {agent_zip}")

# Add name of agent
c.drawString(100, height - 300, f"Name of Agent: {name_of_agent}")

# Add signer's name and title
c.drawString(100, height - 350, f"Signer: {signer_name}, {signer_title}")

# Add conformed signature
c.drawString(100, height - 400, f"Conformed Signature: {conformed_signature}")

# Save PDF
c.save()

# reporting.py

# functions for reporting on the session

# generate a PDF summary of the session - forms completed, any outstanding info, supplemental forms needed, etc.        
def generate_summary(self):
        # Path for the summary log or PDF
        path = "summary.pdf"  # Modify this as required
        
        # Create the PDF with the summary data
        c = canvas.Canvas(path, pagesize=letter)
        width, height = letter
        
        # Add title and other header info
        c.drawString(100, height - 100, "FormWizard: Document Preparation Session Summary")
        
        # Loop through entities_data & filing_data and add to the PDF
        
        # Save the PDF
        c.save()

# Define creation of session id#
def generate_session_id():
    session_id = uuid.uuid4().hex.upper()[0:6]
    return session_id
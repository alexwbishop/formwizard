# pdf_utils.py
# PDF Manipulation Utilities

# Imports
import re
import json
import os
import PyPDF2
import uuid
import logging
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from classes.BaseForm.BaseForm import BaseForm
from classes.Jurisdiction.Jurisdiction import Jurisdiction

# functions

# delete temp folder of unused pdf overlays
def clear_temp_folder():
    confirm = input("Do you want to clear the temp folder? (Y/N): ")
    if confirm.lower() == 'yes':
        for filename in os.listdir('StateForms/completed_forms/temp'):
            os.remove(f'StateForms/completed_forms/temp/{filename}')


# Check if blank PDF template exists
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

# get PDF dimensions
def get_pdf_dimensions(pdf_path):
    try:
        pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
        page = pdf_reader.pages[0]  # Reads the first page
        media_box = page.mediabox
        return media_box.width, media_box.height  
    except Exception as e:
        logging.error(f"An error occurred while reading PDF, {e}")
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

# Define the form key for labeling PDF files being processed, e.g. "DE-Corp-Dom-COA" of file name
form_key = f"{jurisdiction}-{entity_type}-{residency}-{filing_type}"

# Function to merge text PDF onto blank form
# do we need this?

# Merge overlay and form PDFs together
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

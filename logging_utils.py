# logging_utils.py
# Logging configurations and datetime functionalities

# Imports
import re
import json
import os
import PyPDF2
import uuid
import logging
from questions import CAQuestion, DEQuestion
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

# functions

# logging enabled
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='formwizard.log')

# date & time validation
from datetime import datetime
try:
    current_time = datetime.now()
    logging.info(f"Current time: {current_time}")
except Exception as e:
    logging.error(f"An error occurred: {e}")

# Display a complete list of up to 10 entities & forms to be filled
logging.info(f"List of entities/forms to be filled in this session: ")
for i, form in enumerate(forms):
    logging.info(f"{i+1}) form.entity_name - form.entity_type - form.filing_type")


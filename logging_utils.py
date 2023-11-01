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
from classes.BaseForm.base_form import BaseForm
from classes.Jurisdiction.jurisdiction import Jurisdiction

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

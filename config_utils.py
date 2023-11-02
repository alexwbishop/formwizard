# config_utils.py
# JSON Configuration and File Management

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

# JSON configuration function
def load_json_config(file_path):
    try:
    with open('config.json', 'r') as file:
        config = json.load(file)
except FileNotFoundError:
    print("Error: config.json file not found!")
    # Handle the error, e.g., exit the application
except json.JSONDecodeError:
    print("Error: Invalid JSON format in config.json!")
    # Handle the error

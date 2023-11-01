# logging_utils.py
# Logging configurations and datetime functionalities

# Imports
import re
import json
import os
import PyPDF2
import uuid
import logging

# functions

# logging enabled
def message_logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='formwizard.log')

def display_complete_list
# Display a complete list of up to 10 entities & forms to be filled
logging.info(f"List of entities/forms to be filled in this session: ")
for i, form in enumerate(forms):
    logging.info(f"{i+1}) form.entity_name - form.entity_type - form.filing_type")


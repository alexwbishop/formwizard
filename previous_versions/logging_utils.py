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
def message_logging(): 
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='formwizard.log')



# date & time validation
def validate_timestamp():
    from datetime import datetime
    try:
        current_time = datetime.now()
        logging.info(f"Current time: {current_time}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

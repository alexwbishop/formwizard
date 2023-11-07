# reporting.py

# functions for reporting on the session
import logging
import uuid

# Define creation of session id#
def generate_session_id():
    session_id = uuid.uuid4().hex.upper()[0:6]
    return session_id

# logging enabled
def message_logging(): 
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='formwizard.log')


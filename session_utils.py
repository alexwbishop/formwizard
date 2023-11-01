# session_utils.py
# Session Management

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

# Define creation of session id#
def generate_session_id():
    session_id = uuid.uuid4().hex.upper()[0:6]
    return session_id

# Create a session_id for the form prep session
if __name__ == "__main__":
    session_id = generate_session_id()
#  assign the user_id and timestamp to the session markers
form_instance.user_id = user_id
form_instance.session_id = session_id
form_instance.session_timestamp = datetime.now()
logging.info(f"Thank you for authenticating, {user_id}! \n Form prep session initialized. \n Username: {user.id} | Session ID: {session_id}") | Timestamp: {session_timestamp}")



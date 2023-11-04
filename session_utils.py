# session_utils.py
# Form Prep Session Utilities

# Imports
import re
import json
import os
import PyPDF2
import uuid
import logging




# Define creation of session id#
def generate_session_id():
    session_id = uuid.uuid4().hex.upper()[0:6]
    return session_id


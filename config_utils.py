# config_utils.py
# JSON Configuration and File Management

# Imports
import re
import json
import logging

# functions

# JSON configuration function
def load_json_config(file_path):
    try:
    with open('file_path', 'r') as file:
        config = json.load(file)
except FileNotFoundError:
    print("Error: config.json file not found!")
    # Handle the error, e.g., exit the application
except json.JSONDecodeError:
    print("Error: Invalid JSON format in config.json!")
    # Handle the error

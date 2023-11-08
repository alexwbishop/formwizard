# config_utils.py
# JSON Configuration and File Management

# Imports
import json
import logging

# Functions

# Helper function to load JSON configuration
def load_json_config(file_path):
    try:
        with open(file_path, 'r') as file:  # Corrected this line
            config = json.load(file)
            return config  # Return the loaded config
    except FileNotFoundError:
        logging.error("Error: config.json file not found!")
        # Handle the error, e.g., exit the application
        raise
    except json.JSONDecodeError:
        logging.error("Error: Invalid JSON format in config.json!")
        # Handle the error
        raise

class ConfigLoader:
    _instance = None

    @staticmethod
    def get_instance():
        if ConfigLoader._instance is None:
            ConfigLoader()
        return ConfigLoader._instance

    def __init__(self):
        if ConfigLoader._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.config = load_json_config('config.json')
            ConfigLoader._instance = self

    def get(self, key, default=None):
        """Generic getter with a default value if the key is not found."""
        return self.config.get(key, default)

    def get_valid_states(self):
        """Specific getter for the valid states."""
        return self.config.get('VALID_STATES', {})

    def get_validation_rules(self):
        """Specific getter for the validation rules."""
        return self.config.get('VALIDATION_RULES', {})

    # Add more specific getters as needed for different parts of the configuration

# Usage:
# config.get('VALID_STATES', {}) - This will return the VALID_STATES dictionary from the configuration, or an empty dictionary if the key is not found
# config.get_valid_states() - This will return the VALID_STATES dictionary from the configuration, or an empty dictionary if the key is not found
# config.get('VALIDATION_RULES', {}) - This will return the VALIDATION_RULES dictionary from the configuration, or an empty dictionary if the key is not found
# config.get_validation_rules() - This will return the VALIDATION_RULES dictionary from the configuration, or an empty dictionary if the key is not found
# config.get('DEFAULTS', {}) - This will return the DEFAULTS dictionary from the configuration, or an empty dictionary if the key is not found
# config.get_defaults() - This will return the DEFAULTS dictionary from the configuration, or an empty dictionary if the key is not found
# config.get('DEFAULTS', {}).get('domestic_state', Jurisdiction.create_jurisdiction("Delaware", "DE")) - This will return the domestic_state value from the DEFAULTS dictionary, or a Jurisdiction instance if the key is not found
# config.get('DEFAULTS', {}).get('jurisdiction_instance', Jurisdiction.create_jurisdiction("Delaware", "DE")) - This will return the jurisdiction_instance value from the DEFAULTS dictionary, or a Jurisdiction instance if the key is not found

# Usage:
# To access configuration settings, first get the instance of the ConfigLoader
# and then call the getter methods.

# Examples:
# config = ConfigLoader.get_instance().get_config() - This module can be imported wherever you need to access configuration settings, 
# and it will ensure that only one instance of the configuration is active at any given time (Singleton pattern)
# config_loader = ConfigLoader.get_instance()
# valid_states = config_loader.get_valid_states()
# validation_rules = config_loader.get_validation_rules()

# You can also use the generic getter for any other configuration:
# some_config_value = config_loader.get('some_config_key', 'default_value')

# This ensures that you have a consistent way of accessing configuration
# throughout your application, with the added benefit of centralized error handling
# and the ability to add additional processing logic in the getters if needed.
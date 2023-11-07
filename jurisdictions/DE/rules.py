# rules.py
#
# contains functions for validating DE-specific form data
from ...constants.signature_block import SignatureType

# Define the JURISDICTION_RULES using the imported SignatureType
JURISDICTION_RULES = {
    'SIGNATURE_TYPE_ALLOWED': {SignatureType.CONFORMED},
    'EXPEDITE_AVAILABLE': True,
    # ... other rules
}


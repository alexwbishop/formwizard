# jurisdiction.py
#
# contains semi-constant to constant parameters for jurisdiction-related fields 
# i.e. U.S. states, D.C., and local jurisdictions

from constants.signature_block import SignatureType
from constants.states import States

# currently only DE is defined
JURISDICTION_RULES = {
    States.DELAWARE: {
        'SIGNATURE_TYPE_ALLOWED': {SignatureType.CONFORMED},
        'EXPEDITE_AVAILABLE': True,
        'ANNUAL_REPORT_REQUIRED': True,
        # ... other rules
    },
    # ... rules for other states
}

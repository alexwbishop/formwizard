# jurisdiction.py
#
# contains parameters for jurisdiction related fields

from constants.signature_block import SignatureType
from constants.states import State

# currently only DE is defined
JURISDICTION_RULES = {
    State.DELAWARE: {
        'SIGNATURE_TYPE_ALLOWED': {SignatureType.CONFORMED},
        'EXPEDITE_AVAILABLE': True,
        # ... other rules
    },
    # ... rules for other states
}
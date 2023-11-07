# residency.py
from enum import Enum, auto

class Residency(Enum):
    DOMESTIC = auto()
    FOREIGN = auto()

def determine_residency(target_state, filing_state='DELAWARE'):
    # Assuming 'DELAWARE' is the default state for domestic filings and all filings are domestic for now
    if target_state.upper() == filing_state.upper():
        return Residency.DOMESTIC.name
    else:
        return Residency.FOREIGN.name

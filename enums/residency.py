# residency.py
#
from constants import RESIDENCY_OPTIONS
from enum import Enum, auto


class Residency(Enum):
    DOMESTIC = auto()
    FOREIGN = auto()



def determine_filing_nature(target_domestic_state, filing_state=RESIDENCY_OPTIONS['DELAWARE']):
    if target_domestic_state == filing_state:
        return "Domestic"
    else:
        return "Foreign"

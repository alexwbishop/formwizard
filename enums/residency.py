# filing_types.py
#
from enum import Enum, auto
class FilingStatus(Enum):
    DOMESTIC = auto()
    FOREIGN = auto()
    
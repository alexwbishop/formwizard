# filing_statuses.py
#
from enum import Enum, auto
class FilingType(Enum):
    CHANGE_OF_AGENT = auto()
    INCORPORATION = auto()
    REGISTRATION = auto()
    QUALIFICATION = auto()
    WITHDRAWAL = auto()
    CANCELLATION = auto()
    REINSTATEMENT = auto()
    NAME_AMENDMENT = auto()
    STOCK_AMENDMENT = auto()
    ANNUAL_REPORT = auto()
    ADDRESS_UPDATE = auto()
    OFFICIALS_UPDATE = auto()
    MERGER = auto()
    CONVERSION = auto()
    DISSOLUTION = auto()
    CORRECTION = auto()
    BUSINESS_LICENSE = auto()
    MISC_FILING = auto()
    # Add more filing types as needed

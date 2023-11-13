# filing_rules.py
#
from enum import Enum, auto
from constants.name_restrictions import RESTRICTED_WORDS

class FilingTypes(Enum):
    CHANGE_OF_AGENT = auto()
    INCORPORATION = auto()
    REGISTRATION = auto()
    QUALIFICATION = auto()
    WITHDRAWAL = auto()
    CANCELLATION = auto()
    FORMATION = auto()
    REINSTATEMENT = auto()
    NAME_AMENDMENT = auto()
    AMENDMENT = auto()
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
    # ... other enum values ...

# All filing types
FILING_TYPES = {filing_type.name: filing_type for filing_type in FilingTypes}


# Supplemental docs that apply to filing type combinations
# currently only true for filings in DE
FILING_TYPE_SUPPLEMENTAL_DOCS = {
    FilingTypes.REGISTRATION: ['Certificate of Good Standing'],
    FilingTypes.QUALIFICATION: ['Certificate of Good Standing'],
    FilingTypes.WITHDRAWAL: ['Tax Clearance Certificate'],
    FilingTypes.NAME_AMENDMENT: ['Certified Copy of Amendment'],
    # ... other mappings
}

# Checks for supplemental docs
def get_supplemental_docs(filing_type: FilingTypes) -> list:
    return FILING_TYPE_SUPPLEMENTAL_DOCS.get(filing_type, [])


# Questions associated with each filing type - EXAMPLES
FILING_QUESTIONS = {
    FilingTypes.FORMATION: ["General Question 1", "General Question 2"],
    FilingTypes.CHANGE_OF_AGENT: ["General Question 1", "General Question 2"],
    FilingTypes.AMENDMENT: ["Please enter the new name for the entity:"],
    FilingTypes.MERGER: ["Merger-specific Question 1", "Merger-specific Question 2"],
    FilingTypes.CONVERSION: ["Conversion-specific Question 1", "Conversion-specific Question 2"],
    # ... add more for other filing types
}



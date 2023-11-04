# filing_type.py
#
from enum import Enum, auto
from constants.name_restrictions import RESTRICTED_WORDS
from validation import is_valid_entity_name

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
    # ... other enum values ...

# Supplemental docs that apply to filing type combinations
# currently only true for filings in DE
FILING_TYPE_SUPPLEMENTAL_DOCS = {
    FilingType.REGISTRATION: ['Certificate of Good Standing'],
    FilingType.QUALIFICATION: ['Certificate of Good Standing'],
    FilingType.WITHDRAWAL: ['Tax Clearance Certificate'],
    FilingType.NAME_AMENDMENT: ['Certified Copy of Amendment'],
    # ... other mappings
}

# Checks for supplemental docs
def get_supplemental_docs(filing_type: FilingType) -> list:
    return FILING_TYPE_SUPPLEMENTAL_DOCS.get(filing_type, [])


# Validates amended entity name is different from current entity name
def is_valid_new_name(current_name: str, new_name: str) -> bool:
    if current_name == new_name:
        print("The new name cannot be the same as the current name.")
        return False
    for word in RESTRICTED_WORDS:
        if word in new_name:
            print(f"'{word}' is a restricted word for entity names.")
            return False
    return is_valid_entity_name(new_name)

# Questions associated with each filing type - EXAMPLES
FILING_QUESTIONS = {
    FilingType.FORMATION: ["General Question 1", "General Question 2"],
    FilingType.CHANGE_OF_AGENT: ["General Question 1", "General Question 2"],
    FilingType.AMENDMENT: ["Please enter the new name for the entity:"],
    FilingType.MERGER: ["Merger-specific Question 1", "Merger-specific Question 2"],
    FilingType.CONVERSION: ["Conversion-specific Question 1", "Conversion-specific Question 2"],
    # ... add more for other filing types
}



# filing_statuses.py
#
from enum import Enum, auto
from enums.entity_types import EntityType
from constants.name_restrictions import RESTRICTED_WORDS
from validation import is_valid_entity_name
# from PUT ENTITY NAME REFERENCE HERE

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


# supplemental docs that apply to entity type/filing type combinations
# currently only true for filings in DE
FILING_TYPE_SUPPLEMENTAL_DOCS = {
    EntityType.REGISTRATION: ['Certificate of Good Standing'],
    EntityType.QUALIFICATION: ['Certificate of Good Standing'],
    EntityType.WITHDRAWAL: ['Tax Clearance Certificate'],
    EntityType.NAME_AMENDMENT: ['Certified Copy of Amendment'],
    # ... other mappings
}
# checks for supplemental docs
def get_supplemental_docs(filing_type: str) -> list:
    return FILING_TYPE_SUPPLEMENTAL_DOCS.get(filing_type, [])


# validates amended entity name is different from current entity name
def is_valid_new_name(current_name: str, new_name: str) -> bool:
    if current_name == new_name:
        print("The new name cannot be the same as the current name.")
        return False
    for word in RESTRICTED_WORDS:
        if word in entity_name: # NOT YET DEFINED
            print(f"'{word}' is a restricted word for entity names.")
            return False
    return is_valid_entity_name(new_name)

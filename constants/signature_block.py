# signature_block.py
#
# contains parameters for signature block related fields
from enum import Enum, auto

# methods of document execution
class SignatureType(Enum):
    PDF_SCAN = auto()
    CONFORMED = auto()
    HARD_COPY = auto()
    NOTARIZED = auto()
    TYPE_IN = auto()
    E_SIGNATURE = auto()
    # ... add other signature types

# signer title matches with entity type
ENTITY_TITLE_MATCH = {
    'LLC': ['Manager', 'Member', 'Authorized Person'],
    'Corp': ['CEO', 'President', 'Treasurer', 'Vice President', "COO", "Chief Operating Officer", 
             "Chief Executive Officer", "Executive Vice President", "Chief Executive Officer",
             'Secretary', 'Director', 'Assistant Secretary', "CFO", "Chief Financial Officer", "Assistant Treasurer"],
    'LP': ['General Partner', 'Limited Partner'],
    'GP': ['General Partner'],
    'LLP': ['General Partner', 'Limited Partner'],
    'WITH_POA': ['Power of Attorney', 'Attorney in Fact', 'Authorized Person']
}

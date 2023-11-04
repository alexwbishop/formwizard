# signature_block.py
#
# contains parameters for signature block related fields

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
             'Secretary', 'Director', 'Assistant Secretary', "CFO", "Chief Financial Officer", "Assistant Treasurer",
    'LP': ['General Partner', 'Limited Partner'],
    'GP': ['General Partner'],
    'LLP': ['General Partner', 'Limited Partner'],
    'WITH_POA': ['Power of Attorney', 'Attorney in Fact', 'Authorized Person']
        ]
    }
# validate signer title matches with entity type
def is_valid_signer_title(entity_type: str, title: str) -> bool:
    if title not in ENTITY_TITLE_MATCH.get(entity_type, []):
        print(f"'{title}' is not a valid title for {entity_type}.")
        return False
    return True

# validate signer name is an individual's name
def is_valid_signer_name(name: str) -> bool:
    if 1 < len(name.split()) <= 2:  # expecting a first and last name
        return True
    print("Signer name does not seem to be a valid individual's name.")
    return False

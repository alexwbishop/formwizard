# document_types.py
#
from enum import Enum, auto
class DocumentTypes(Enum):
    CERTIFICATE_OF_GOOD_STANDING = auto()
    ANNUAL_REPORT = auto()
    CERTIFIED_COPY_OF_EVIDENCE = auto()
    CERT_RE_OF_EVIDENCE = auto()
    CERTIFIED_COPY_OF_ARTICLES = auto()
    POWER_OF_ATTORNEY = auto()
    TAX_CLEARANCE_CERT = auto()
    NAME_RESERVATION_CERT = auto()
    PRIMARY_FORM = auto()
    SECONDARY_FORM = auto()
    SUPPLEMENTAL_FORM = auto()
    OFFICER_DIRECTOR_LIST = auto()
    MANAGER_MEMBER_LIST = auto()
    FRANCHISE_TAX_FORM = auto()
    NAME_CLEARANCE_LETTER = auto()
    # Add more document types as needed
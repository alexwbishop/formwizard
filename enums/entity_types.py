# entity_types.py
#
from enum import Enum, auto
class EntityType(Enum):
    LIMITED_LIABILITY_COMPANY = auto()
    CORPORATION = auto() # for-profit corporation or stock corporation
    LIMITED_PARTNERSHIP = auto()
    NONPROFIT_CORPORATION = auto()
    LIMITED_LIABILITY_PARTNERSHIP = auto()
    LIMITED_LIABILITY_LIMITED_PARTNERSHIP = auto()
    BENEFIT_COMPANY = auto()
    COOPERATIVE = auto()
    STATUTORY_TRUST = auto()
    BUSINESS_TRUST = auto()
    # Add more entity types as needed
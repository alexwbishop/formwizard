# states.py
#
from enum import Enum, auto
class States(Enum):
    DELAWARE = ('DE', 'Delaware')
    CALIFORNIA = ('CA', 'California')
    # currently capable states above

    # unsupported states below
    ALABAMA = ('AL', 'Alabama')
    ALASKA = ('AK', 'Alaska')
    ARIZONA = ('AZ', 'Arizona')
    ARKANSAS = ('AR', 'Arkansas')
    #CALIFORNIA = ('CA', 'California') - moved up
    COLORADO = ('CO', 'Colorado')
    CONNECTICUT = ('CT', 'Connecticut')
    #DELAWARE = ('DE', 'Delaware') - moved up
    FLORIDA = ('FL', 'Florida')
    GEORGIA = ('GA', 'Georgia')
    HAWAII = ('HI', 'Hawaii')
    IDAHO = ('ID', 'Idaho')
    ILLINOIS = ('IL', 'Illinois')
    INDIANA = ('IN', 'Indiana')
    IOWA = ('IA', 'Iowa')
    KANSAS = ('KS', 'Kansas')
    KENTUCKY = ('KY', 'Kentucky')
    LOUISIANA = ('LA', 'Louisiana')
    MAINE = ('ME', 'Maine')
    MARYLAND = ('MD', 'Maryland')
    MASSACHUSETTS = ('MA', 'Massachusetts')
    MICHIGAN = ('MI', 'Michigan')
    MINNESOTA = ('MN', 'Minnesota')
    MISSISSIPPI = ('MS', 'Mississippi')
    MISSOURI = ('MO', 'Missouri')
    MONTANA = ('MT', 'Montana')
    NEBRASKA = ('NE', 'Nebraska')
    NEVADA = ('NV', 'Nevada')
    NEW_HAMPSHIRE = ('NH', 'New Hampshire')
    NEW_JERSEY = ('NJ', 'New Jersey')
    NEW_MEXICO = ('NM', 'New Mexico')
    NEW_YORK = ('NY', 'New York')
    NORTH_CAROLINA = ('NC', 'North Carolina')
    NORTH_DAKOTA = ('ND', 'North Dakota')
    OHIO = ('OH', 'Ohio')
    OKLAHOMA = ('OK', 'Oklahoma')
    OREGON = ('OR', 'Oregon')
    PENNSYLVANIA = ('PA', 'Pennsylvania')
    RHODE_ISLAND = ('RI', 'Rhode Island')
    SOUTH_CAROLINA = ('SC', 'South Carolina')
    SOUTH_DAKOTA = ('SD', 'South Dakota')
    TENNESSEE = ('TN', 'Tennessee')
    TEXAS = ('TX', 'Texas')
    UTAH = ('UT', 'Utah')
    VERMONT = ('VT', 'Vermont')
    VIRGINIA = ('VA', 'Virginia')
    WASHINGTON = ('WA', 'Washington')
    WEST_VIRGINIA = ('WV', 'West Virginia')
    WISCONSIN = ('WI', 'Wisconsin')
    WYOMING = ('WY', 'Wyoming')
    DISTRICT_OF_COLUMBIA = ('DC', 'District of Columbia')

def __init__(self, abbrev, full):
        self.abbrev = abbrev
        self.full = full

# Accessing the values
#print(States.DELAWARE.abbrev)  # Output: DE
#print(States.DELAWARE.full)     # Output: Delaware

# ALL STATES
VALID_STATES = {States.DELAWARE, States.CALIFORNIA, States.ALASKA, States.ARIZONA, States.ARKANSAS, States.COLORADO, States.CONNECTICUT, States.FLORIDA, States.GEORGIA, States.HAWAII, States.IDAHO, States.ILLINOIS, States.INDIANA, States.IOWA, States.KANSAS, States.KENTUCKY, States.LOUISIANA, States.MAINE, States.MARYLAND, States.MASSACHUSETTS, States.MICHIGAN, States.MINNESOTA, States.MISSISSIPPI, States.MISSOURI, States.MONTANA, States.NEBRASKA, States.NEVADA, States.NEW_HAMPSHIRE, States.NEW_JERSEY, States.NEW_MEXICO, States.NEW_YORK, States.NORTH_CAROLINA, States.NORTH_DAKOTA, States.OHIO, States.OKLAHOMA, States.OREGON, States.PENNSYLVANIA, States.RHODE_ISLAND, States.SOUTH_CAROLINA, States.SOUTH_DAKOTA, States.TENNESSEE, States.TEXAS, States.UTAH, States.VERMONT, States.VIRGINIA, States.WASHINGTON, States.WEST_VIRGINIA, States.WISCONSIN, States.WYOMING, States.DISTRICT_OF_COLUMBIA}

# Define the currently supported states
SUPPORTED_STATES = {States.DELAWARE, States.CALIFORNIA}


# Check if a state is supported
def is_state_supported(state):
    return state in SUPPORTED_STATES

# Example usage
#print(is_state_supported(States.DELAWARE))  # Output: True
#print(is_state_supported(States.TEXAS))     # Output: False (assuming Texas is not in the SUPPORTED_STATES set)

# 
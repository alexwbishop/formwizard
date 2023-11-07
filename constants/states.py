# states.py
#
from enum import Enum, auto
class State(Enum):
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
#print(State.DELAWARE.abbrev)  # Output: DE
#print(State.DELAWARE.full)     # Output: Delaware

# ALL STATES
VALID_STATES = {State.DELAWARE, State.CALIFORNIA, State.ALASKA, State.ARIZONA, State.ARKANSAS, State.COLORADO, State.CONNECTICUT, State.FLORIDA, State.GEORGIA, State.HAWAII, State.IDAHO, State.ILLINOIS, State.INDIANA, State.IOWA, State.KANSAS, State.KENTUCKY, State.LOUISIANA, State.MAINE, State.MARYLAND, State.MASSACHUSETTS, State.MICHIGAN, State.MINNESOTA, State.MISSISSIPPI, State.MISSOURI, State.MONTANA, State.NEBRASKA, State.NEVADA, State.NEW_HAMPSHIRE, State.NEW_JERSEY, State.NEW_MEXICO, State.NEW_YORK, State.NORTH_CAROLINA, State.NORTH_DAKOTA, State.OHIO, State.OKLAHOMA, State.OREGON, State.PENNSYLVANIA, State.RHODE_ISLAND, State.SOUTH_CAROLINA, State.SOUTH_DAKOTA, State.TENNESSEE, State.TEXAS, State.UTAH, State.VERMONT, State.VIRGINIA, State.WASHINGTON, State.WEST_VIRGINIA, State.WISCONSIN, State.WYOMING, State.DISTRICT_OF_COLUMBIA}

# Define the currently supported states
SUPPORTED_STATES = {State.DELAWARE, State.CALIFORNIA}


# Check if a state is supported
def is_state_supported(state):
    return state in SUPPORTED_STATES

# Example usage
#print(is_state_supported(State.DELAWARE))  # Output: True
#print(is_state_supported(State.TEXAS))     # Output: False (assuming Texas is not in the SUPPORTED_STATES set)

# 
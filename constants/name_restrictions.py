# name_restrictions.py
#
# words that are generally restricted or prohibited from use in entity names, statewide
#
PROHIBITED_WORDS = ["Federal", "Trust", "National", "United States", "Reserve", 
                    "America", "American", "US", "USA", "USAA", "OLYMPIC", "PARALYMPIC",  
                    "USAA Savings Bank", "USAA Federal Savings Bank", "USAA Federal Savings Bank",
                    ]
#
AUTHORIZED_WORDS =  ["Bank", "Bancorp", "Bancorporation", "INSURANCE", "BROKER", "ENGINEER"] 
#
#
# create combination of red flag words to be used in name validation
RESTRICTED_WORDS = (
    PROHIBITED_WORDS + AUTHORIZED_WORDS
)
#
MAX_PURPOSE_LENGTH = 500  # example length, adjust as needed




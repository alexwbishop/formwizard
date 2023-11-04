# entity_indicators.py
#
# Entity Type Indicators
ENTITY_INDICATORS_LLC = [
    "LLC", "LIMITED LIABILITY COMPANY", "L.L.C.", "L.L.C", "LTD LIABILITY CO", "LTD LIABILITY COMPANY"
]

ENTITY_INDICATORS_LP = [
    "LIMITED PARTNERSHIP", "LP", "L.P.", "L.P",
]

ENTITY_INDICATORS_CORP = [
    "CORP", "CORPORATION", "INC", "INCORPORATED", "CO", "COMPANY"
]

ENTITY_INDICATORS_LLP = [
    "LLP", "L.L.P.", "L.L.P", "LIMITED LIABILITY PARTNERSHIP"
]

ENTITY_INDICATORS_PLC = [
    "PLLC", "P.L.L.C.", "P.L.L.C", "PLC", "P.L.C.", "P.L.C", "PROFESSIONAL LIMITED LIABILITY COMPANY"
]

ENTITY_INDICATORS_LLLP = [
    "LLLP" "L.L.L.P.", "L.L.L.P" "LIMITED LIABILITY LIMITED PARTNERSHIP"
]
# Combine all indicators into one list for easy import and use
VALID_ENTITY_INDICATORS = (
    ENTITY_INDICATORS_LLC +
    ENTITY_INDICATORS_LP +
    ENTITY_INDICATORS_CORP +
    ENTITY_INDICATORS_LLP +
    ENTITY_INDICATORS_PLC +
    ENTITY_INDICATORS_LLLP
)
# boolean.py
# 
def ask_yes_no_question(question_key, jurisdiction):
    # Retrieve the question mapping based on the key and jurisdiction
    answer = JURISDICTION_RULES[question_key].get(jurisdiction, False)
    return answer
#


# Example of boolean constants for general conditions
GENERAL_RULES = {
    'AGENT_CONSENT_NEEDED': ['SC', 'WA'],
    'ANNUAL_REPORT_APPLIES': ['DE', 'TX'],
    # ... other rules
}

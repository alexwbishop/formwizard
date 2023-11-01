# questions.py
# Questions and State Handling

#Steps to Populate questions.py:
    #Identify Question Points: Scan your current codebase to identify where you're asking for user input. This can be as simple as calls to input() or more complex UI components.
    #Generalize Questions: If you notice that you're asking similar types of questions across the board, you could generalize them into a single function.
#For example, if you have multiple Yes/No questions, you could have a general ask_yes_no_question() function.
    #Validation Functions: If you have validation logic right next to the question prompt, consider abstracting these into separate functions and moving them into questions.py.
    #State-Specific Questions: Since you have a hierarchy that goes from BaseForm up to Jurisdiction and FilingType,
  #consider adding methods in your Question class (or its subclasses) that generate state or filing type-specific questions.
    #Inheritance and Overriding: If different jurisdictions have slightly different requirements for the same kind of question,
#use inheritance to create a base version of the question in the Question class, and override it in each state-specific subclass as needed.

# Imports
import re
import json
import os
import PyPDF2
import uuid
import logging
from questions import CAQuestion, DEQuestion
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from classes.BaseForm.base_form import BaseForm
from classes.Jurisdiction.jurisdiction import Jurisdiction

# functions



# lines of questioning

class BaseQuestion:
    def common_questions(self):
        # Code for questions that are common across all states
        pass

class CAQuestion(BaseQuestion):
    def state_specific_questions(self):
        # California specific questions
        pass

    def all_questions(self):
        self.common_questions()
        self.state_specific_questions()

class DEQuestion(BaseQuestion):
    def state_specific_questions(self):
        # Delaware specific questions
        pass

    def all_questions(self):
        self.common_questions()
        self.state_specific_questions()

def ask_yes_no_question(prompt):
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Invalid response. Please enter 'y' or 'n'.")




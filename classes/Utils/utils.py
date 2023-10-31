# utils.py
#
#The Utils class and its subclasses are designed to encapsulate utility functions that can be used across different parts of your application. 
#These are often methods that don't necessarily belong to any of the domain-specific classes like BaseForm or EntityType, but are still essential for the functioning of your application.
# (The idea is to separate concerns and make the code more modular and easier to manage. Utility classes like these can be very helpful for that.)

#Utils: This would be a general utility class. It might not have any specific attributes or methods but serves as a base class for more specific utility classes.
class Utils:
#Methods: These are example methods that each utility class might have. For instance, pdf_related_method() could be a method in PDFUtils that handles a specific PDF-related task.
    def pdf_related_method(self):
        pass
#Similarly, validation_related_method() could be a method in ValidationUtils that handles a specific validation task.
    def validation_related_method(self):
        pass
#PDFUtils: This subclass would contain methods related to PDF manipulation. For example, methods for filling out a PDF, saving a PDF, merging PDFs, etc., would go here.
class PDFUtils(Utils):
    pass
#ValidationUtils: This subclass would contain methods related to data validation. For example, methods for checking if a given input is valid, if a required field is filled out, etc., would go here.
class ValidationUtils(Utils):
    pass


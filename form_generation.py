# form_generation.py
#
# Functions relating to generating forms based on user input

#functions relating to PDF generation - these are not defined - why?
print("Checking file path...", form_template_path, "...")
check_file_path(form_template_path)
# Function to get PDF dimensions
print("Getting PDF dimensions...")
get_pdf_dimensions(pdf_path)
# Function to populate form fields
print("Populating form fields for: ", entity_name) 
populate_form()
# Function to merge text PDF onto blank form
print("Merging responses onto blank form fields...")
# PDF is then exported to the ./completed_forms directory
merge_overlay_pdf()
print("Form generation for", entity_name, "is complete!")
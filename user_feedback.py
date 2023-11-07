# user_feedback.py

# Functions relating to asking for user experience feedback and logging it

# record user feedback collection on the session - save to a dedicated log file
def collect_feedback(self):
        rating = input("On a scale of 1-10, how would you rate your experience with FormWizard? ")
        
        # Validate rating
        while not rating.isdigit() or not 1 <= int(rating) <= 10:
            rating = input("Please provide a valid rating between 1 and 10: ")
        
        comments = input("Any additional comments or suggestions? ")
        
        with open("feedback_log.txt", "a") as f:
            f.write(f"Rating: {rating}\nComments: {comments}\n\n")
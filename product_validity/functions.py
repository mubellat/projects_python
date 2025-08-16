from datetime import datetime

def today():
    today = datetime.now()
    return today

def verify_date(date):
    try: 
        date_format = datetime.strptime(date, "%d-%m-%Y") # datetime parameters module
        return date_format
    except:
        raise Exception("Invalid input. Suggested format: dd/mm/yy\nExample: 22.03.2024") # stops the entire program
        # error handling for developers

def verify_due(date_ref):
    due_date = verify_date(date = date_ref) # converts user input to the format
    if today() > due_date:
        return "Date expired..."
    else:
        return "Date not expired..."
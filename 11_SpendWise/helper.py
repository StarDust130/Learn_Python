
from datetime import datetime




def format_date(date_str):
    # Convert the string to a datetime object
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    # Format the date to dd-mm-yyyy
    return date_obj.strftime("%d-%m-%Y")

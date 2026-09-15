import datetime
import pytz

def get_current_indian_date():
    tz = pytz.timezone('Asia/Kolkata')
    
    # Get the current UTC time
    utc_now = datetime.datetime.utcnow()
    
    # Convert the UTC time to IST
    ist_now = utc_now.astimezone(tz)
    
    # Extract the date from the IST time
    indian_date = ist_now.date()
    
    return indian_date
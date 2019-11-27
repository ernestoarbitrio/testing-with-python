from datetime import datetime

def get_now():
    return datetime.now()

def get_today():
    return datetime.today()

def is_weekday():
    today = get_today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

def is_summer():
    month = get_now().month
    return month in [6, 7, 8]
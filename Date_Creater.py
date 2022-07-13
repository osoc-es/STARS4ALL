from datetime import datetime

def current_date_format():
    date = datetime.now()
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month = months[date.month - 2]
    year = date.year
    messsage = "{}-{}".format( month, year)

    return messsage


print(current_date_format())
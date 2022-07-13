from datetime import datetime

#This funtion is designed so we can access to the time of the last month before 
    #the activation of the main, so we can use it to obtein the name of the file and path.

def current_date_format():
    date = datetime.now()
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    month = months[date.month - 2]
    year = date.year
    messsage = "{}-{}".format( month, year)

    return messsage


print(current_date_format())
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta


def date_list():
    list_dates=[]
    inicio='2016-08-01T00:00:00Z'
    date = datetime.strptime(inicio,'%Y-%m-%dT%H:%M:%SZ')
    for i in range(72):
        a=date + relativedelta(months=i)
        list_dates.append( a.strftime('%Y-%m-%dT%H:%M:%SZ'))
    return(list_dates)
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

def date_list(inicio,fin):
    list_dates=[]
    date_inicio = datetime.strptime(inicio,'%Y-%m-%dT%H:%M:%SZ')
    date_fin = datetime.strptime(fin,'%Y-%m-%dT%H:%M:%SZ')
    while date_inicio != date_fin:
        date_inicio=date_inicio + relativedelta(months=1)
        list_dates.append(date_inicio.strftime('%Y-%m-%dT%H:%M:%SZ'))
    return(list_dates)

print(date_list('2016-08-01T00:00:00Z','2022-06-01T00:00:00Z'))
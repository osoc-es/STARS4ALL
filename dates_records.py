from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys

def date_list(inicio,fin):
    list_dates=[]
    date_inicio = datetime.strptime(inicio,'%Y-%m-%dT%H:%M:%SZ')
    date_fin = datetime.strptime(fin,'%Y-%m-%dT%H:%M:%SZ')
    while date_inicio != date_fin:
        date_inicio=date_inicio + relativedelta(months=1)
        list_dates.append(date_inicio.strftime('%Y-%m-%dT%H:%M:%SZ'))
    return(list_dates)

if __name__ == "__main__":

        date_list(sys.argv[1], sys.argv[2])

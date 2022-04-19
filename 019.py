#019

from datetime import datetime
from dateutil.relativedelta import relativedelta

#매월1일이 일요일인 경우 count
def count_sunday(start, end): #yyyy-mm-dd 형식으로
    count = 0
    date = datetime.strptime(start, '%Y-%m-%d')
    while date <= datetime.strptime(end, '%Y-%m-%d'):
        
        if date.weekday() == 6:
            count += 1
        delta = relativedelta(months=1)
        date = date + delta
    return count

count_sunday('1901-01-01', '2000-12-31')
#--------------------------------------------------
#answer 171
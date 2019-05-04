from datetime import date, timedelta

def last_day_from_week(last_day, year=0, month=0, day=0):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']

    last_day = (last_day[0].upper()+last_day[1:].lower())

    if(year == 0 and month == 0 and day == 0):
        curday = date.today()
    else:
        curday = date(year,month,day)

    if(curday.isoweekday() == (days_of_week.index(last_day) + 1)):
        return curday.strftime("%Y%m%d")
    elif((curday.isoweekday()-1) == (days_of_week.index(last_day) + 1)):
        return  (curday - timedelta(1)).strftime("%Y%m%d")
    elif((curday.isoweekday()-2) == (days_of_week.index(last_day) + 1)):
        return (curday - timedelta(2)).strftime("%Y%m%d")
    elif((curday.isoweekday()-3) == (days_of_week.index(last_day) + 1)):
        return (curday - timedelta(3)).strftime("%Y%m%d")
    elif((curday.isoweekday()-4) == (days_of_week.index(last_day) + 1)):
        return (curday - timedelta(4)).strftime("%Y%m%d")
    else:
        idx = (curday.isoweekday()%7)
        last_date = (curday - timedelta(7 + idx - (days_of_week.index(last_day) + 1)))
    return last_date.strftime("%Y%m%d")
firstSundays = 0

day = 0 # Every day is given a number, indexed from 0 at 1 Jan 1900
date = 0 # Date of the month (0-30)
month = 0 # Current working month (0-11)
year = 1900 # Current year

while True:
    if year >= 2001: #Stop after 31 Dec 2000
        break
    if date == 0 and year >= 1901 and day % 7 == 6: # If a Sunday and first day of month and after 31 Dec 1900 (since we know 1 Jan 1900 is a Monday)
        firstSundays += 1

    # Now advance everything by one day
    if month in [3,5,8,10]: # If current month has 30 days
        if date >= 29:
            date = 0
            month += 1
        else:
            date += 1
    elif month == 1: # If February
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0): # If a leap year
            if date >= 28:
                date = 0
                month += 1
            else:
                date += 1
        else:
            if date >= 27:
                date = 0
                month += 1
            else:
                date += 1
    elif month == 11: # If December
        if date >= 30:
            date = 0
            month = 0
            year += 1
        else:
            date += 1
    else: # If any other boring 31-day month
        if date >= 30:
            date = 0
            month += 1
        else:
            date += 1

    day += 1

print(firstSundays)

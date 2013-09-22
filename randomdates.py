from datetime import date
import random

def generate_random_dates(startyear = 1900, startmonth = 1, startday = 1,
                        endyear = 2013, endmonth = 12, endday = 31,
                        today = True,
                        numberofdates = 1):
    """
    Method returns a list of n dates between a specified start, and end date.
    n corresponds to the numberofdates named parameter.

    Dates are in the yyyy-mm-dd format.

    By default it returns one random date between 1900-01-01 and today's date.

    If today is set to False, it returns a date between 1900-01-01 and a
    specific end date.

    Returned dates are uniformly distributed between the start and end dates.

    Throws ValueError if date initialization is incorrect.
    """

    try:
        newdatelist = []
        if numberofdates < 1: numberofdates = 1 #always returns one date
        numberofdates = int(numberofdates) #prevents TypeError in case of fractional values
        
        startdate = date(startyear, startmonth, startday)
        startdateordinal = startdate.toordinal()
        if today:
            enddate = date.today()
            enddateordinal = enddate.toordinal()
        else:
            enddate = date(endyear, endmonth, endday)
            enddateordinal = enddate.toordinal()

##        print "Start date, and ordinal:", startdate, startdateordinal
##        print "End date, and ordinal:", enddate, enddateordinal
##        print "Generating %s random dates" % numberofdates

        for i in range(numberofdates):
            newdateordinal = random.randrange(startdateordinal, enddateordinal)
            newdate = date.fromordinal(newdateordinal)
            newdatelist.append(newdate)
        print "Date generation completed!"
        return newdatelist
    
    except ValueError as e:
        print "Incorrect date component given."
        print "Start date: %s, %s, %s, End date: %s, %s, %s is not valid." % \
        (startyear, startmonth, startday, endyear, endmonth, endday)
    
##Uncomment lines below for testing the above method.
##print generate_random_dates(numberofdates = 10) #must generate 10 dates between 1900-01-01, and today.
##print generate_random_dates(numberofdates = 0.5) #must generate 1 date between 1900-01-01, and today.
##print generate_random_dates(numberofdates = -1) #must generate 1 date between 1900-01-01, and today.
##print generate_random_dates(numberofdates = 10, today = False) #must generate 10 dates between 1900-01-01, and 2013-12-31.
##print generate_random_dates(numberofdates = 10, startday = 40) #ValueError exception must be handled.


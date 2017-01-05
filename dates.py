#!/usr/bin/python

# Inspired by question by Websten from Udacity cs101 forums
#
          
def isLeapYear(year):
    
    
    #Does the year end in 00, like 1800, 1900, etc.  If it does is it divisible by 400?  If it is then it is a 
    #leap year.  Otherwise it is not a leap year.  1900 is not a a leap year because 1900 / 400 == 4.75.
    #2000 / 400 == 5 so 2000 is a leap year.
    #If the year does not end in 00, e.g. 2016, is it divisible by 4.  If it is it is a leap year
    
    LeapYear = False
    
    if year % 100 == 0:
        if year % 400 == 0:
            LeapYear = True
            return LeapYear
        return LeapYear
    if year % 4 == 0:
        LeapYear = True
        return LeapYear
    return LeapYear

def daysInMonth(year,month):
    
    """returns number of days in month, taking into account leap years"""
    
    days = 0
    
    #add a 0 month as a place holder so that we can use natural month numbers instead of starting
    #at month 0
    numberOfDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]
 
    LeapYear = isLeapYear(year)
    if LeapYear:
        if month == 2:
            days = numberOfDays[month] + 1
            return days
    days = numberOfDays[month]
    return days

def isValidDate(year1, month1, day1, year2, month2, day2):
    """Do date validation. Return True if date is valid else return False"""
    
    if year1 <= 0:
        return False
    if year2 <= 0:
        return False
    if month1 < 1:
        return False
    if month1 > 12:
        return False
    if month2 > 12:
        return False
    if month2 < 1:
        return False
    if day1 < 1:
        return False
    if day2 < 1:
        return False
        
    if day1 > daysInMonth(year1, month1):
        return False
    if day2 > daysInMonth(year2, month2):
        return False
        
    return True

def orderDateRange(year1, month1, day1, year2, month2, day2):
    
    """We need to get the dates ordered such that date1 < date2
    if year1 < year2 then all the dates get swapped
    if year1 == year2 then we need to have month1 < month2
    if year1 == year2 and month1 == month2 then we need to have day1 < day2"""
    
    if year2 < year1:
        year1, month1, day1, year2, month2, day2 = year2, month2, day2, year1, month1, day1
        return year1, month1, day1, year2, month2, day2
        
    if year2 == year1:
        if month2 < month1:
            month1, day1, month2, day2 = month2, day2, month1, day1
            return year1, month1, day1, year2, month2, day2
            
    if year2 == year1:
        if month2 == month1:
            if day2 < day1:
                day1, day2 = day2, day1
                return year1, month1, day1, year2, month2, day2
                
    return year1, month1, day1, year2, month2, day2

def daysInYear(year):
    """Return number of days in the year passed in"""
    if isLeapYear(year):
        return 366
    return 365
    
def daysLeftInMonth(year, month, day):
    """Return the number of days left in the month"""
    
    daysInThisMonth = daysInMonth(year, month)
    daysLeft = daysInThisMonth - day
    return daysLeft
    
def daysGoneInYear(year, month, day):
    """Number of days which have passed since beginning of current year"""
    
    thisYear = year
    thisMonth = month
    monthBeingCounted = 1
    today = day
    
    daysGone = today
    
    while monthBeingCounted < thisMonth :
        daysGone = daysGone + daysInMonth(thisYear, monthBeingCounted)
        monthBeingCounted += 1
    
    return daysGone

def daysLeftInYear(year, month, day):
    
    #Subtract days gone in this year from number of days in this year to get number of remaining days
    
    daysLeft = daysInYear(year) - daysGoneInYear(year, month, day)
    
    return daysLeft
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    
    """We are counting how many days are between given dates
    Are the dates in the same calendar year?  If so just calculate the days in between the days of the
    2 given months.
    Are the dates in adjacent calendar months? If so we calculate the days left in month1 and add them
    to the days gone in month2 (which is the day given for month2)
    Are the dates in adjacent calendar years?  If so we calculate the days left in year1 and add them
    to the days gone in year2
    Are the dates given in 2 different calendar years?  If so calculate the number of days left in year1.
    Next calculate the days gone in year 2.
    Next add-up all the days between year1 and year2 and add those days to the total.
    So we get daysLeftInYear + daysGoneInYear + daysBetweenYears"""
    
    if not (isValidDate(year1, month1, day1, year2, month2, day2)):
        return -1
    
    #make sure date1 < date2
    year1, month1, day1, year2, month2, day2 = orderDateRange(year1, month1, day1, year2, month2, day2)
    
    yearsToCount = year2 - year1
    
    totalDays = 0
    
    if yearsToCount == 0: #are the dates in the same calendar year
        monthsToCount = month2 - month1
        if monthsToCount == 0:
            totalDays = day2 - day1
            return totalDays
        if monthsToCount == 1: #are the dates in adjacent months
            totalDays = daysLeftInMonth(year1, month1, day1) + day2
            return totalDays
        
        #Is there 1 whole calendar month between the given dates?
        counter = month1 + 1
        while counter < month2:
            totalDays += daysInMonth(year1, counter)
            counter += 1
        totalDays += (daysLeftInMonth(year1, month1, day1) + day2)
        return totalDays
        
    if yearsToCount == 1: #are the dates in adjacent calendar years
        totalDays = daysLeftInYear(year1, month1, day1) + daysGoneInYear(year2, month2, day2)
        return totalDays
    
    #Is there at least 1 whole calendar year between the dates?
    yearCounter = year1 + 1
    while yearCounter < year2:
        totalDays += daysInYear(yearCounter)
        yearCounter += 1
    totalDays = daysLeftInYear(year1, month1, day1) + daysGoneInYear(year2, month2, day2) + totalDays
    return totalDays

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

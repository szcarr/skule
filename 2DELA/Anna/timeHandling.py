from datetime import datetime
from calendar import monthrange

'''
A simple file to handle dates and time.
'''

def getCurrentTime():

    '''
    Returns a string with UTC time
    Can split time by ":" to get hours,minutes,seconds separately
    '''

    splitList = getUTCtime().split(" ")
    return splitList[1]

def getDateToday():

    '''
    Returns a string with today's date in the format YYYY-MM-DD
    '''

    splitList = getUTCtime().split(" ")
    return splitList[0]

def getHoursMinutesSeconds(time):

    '''
    Parameter should be in the format HH-MM-SS

    Returns a list with the time.
    Where each value is separated.
    Index 0 = Hours.
    Index 1 = Minutes.
    Index 2 = Seconds.
    '''
    
    timeList = []
    for unit in str(time).split(":"):
        timeList.append(round(float(unit)))

    return timeList


def getUTCtime():

    '''
    Returns a string with current date and time
    Can split string by " " to get date and time separately
    '''

    return str(datetime.utcnow())

def getYearMonthDay(date):

    '''
    Parameter should be in the format YYYY-MM-DD

    Returns a list with the date.
    Where each value is separated.
    Index 0 = Year.
    Index 1 = Month.
    Index 2 = Day.
    '''

    date = str(date).split("-")
    dateList = []
    for numbers in date:
        dateList.append(int(numbers))

    return dateList

def checkIfTimeRightNowHasPassedArgumentTime(dateAndTime):

    '''
    dateAndTime parameter should be 'YYYY-MM-DD HH:MM:SS'.\n
    Compares if the date and time passed as an argument is in the past.\n 
    Remember, function uses UTC time!
    If true:
    returns true.
    \n
    Else:
    returns false.
    \n
    Parameters:\n
    dateCompared should be passed in the format YYYY-MM-DD. 
    dateCompared should be a string. 
    \n
    timeCompared should be passed in the format HH:MM:SS. 
    timeCompared should be a string.
    '''

    dateList = str(dateAndTime).split(" ")
    date = dateList[0]
    time = dateList[1]
    dateCompared = getYearMonthDay(date)
    dateNow = getYearMonthDay(getDateToday())

    timeCompared = getHoursMinutesSeconds(time)
    timeNow = getHoursMinutesSeconds(getCurrentTime())

    #Checking if year month or day is
    #print(dateCompared[0], dateNow[0])
    if dateCompared[0] < dateNow[0]:
        return True

    #print(dateCompared[1], dateNow[1])
    if dateCompared[0] <= dateNow[0] and dateCompared[1] < dateNow[1]:
        return True

    #print(dateCompared[2], dateNow[2])
    if dateCompared[0] <= dateNow[0] and dateCompared[1] <= dateNow[1] and dateCompared[2] < dateNow[2]:
        return True

    #Checking time
    #print(timeCompared[0], timeNow[0])
    if dateCompared[0] <= dateNow[0] and dateCompared[1] <= dateNow[1] and dateCompared[2] <= dateNow[2] and timeCompared[0] < timeNow[0]:
        return True
    
    #print(timeCompared[1], timeNow[1])
    if dateCompared[0] <= dateNow[0] and dateCompared[1] <= dateNow[1] and dateCompared[2] <= dateNow[2] and timeCompared[0] <= timeNow[0] and timeCompared[1] < timeNow[1]:
        return True

    #print(timeCompared[2], timeNow[2])
    if dateCompared[0] <= dateNow[0] and dateCompared[1] <= dateNow[1] and dateCompared[2] <= dateNow[2] and timeCompared[0] <= timeNow[0] and timeCompared[1] <= timeNow[1] and timeCompared[2] < timeNow[2]:
        return True

    return False

def scheduleTime(dateAndTime, **kwargs):

    '''
    timeAndDate is the time you want to modify.\n
    Passed in the form 'YYYY-MM-DD HH:MM:SS' as a string.\n
    Like the function getUTCtime().\n

    kwargs are the unit and value you want to add to dateAndTime.\n
    Examples: year = 0, month = 0, day = 1, hours = 1, minutes = 0, seconds = 0
    '''    

    splitList = str(dateAndTime).split(" ")
    #print(splitList)
    yearMonthDay = getYearMonthDay(splitList[0])
    hoursMinutesSeconds = getHoursMinutesSeconds(splitList[1])

    listWithKeys = list(kwargs.keys())

    for d in range(len(yearMonthDay)):
        for k in range(len(listWithKeys)):
            if d == 0 and listWithKeys[k] == "year":
                yearMonthDay[d] = yearMonthDay[d] + int(kwargs.get(listWithKeys[k]))
            elif d == 1 and listWithKeys[k] == "month":
                yearMonthDay[d] = yearMonthDay[d] + int(kwargs.get(listWithKeys[k]))
            elif d == 2 and listWithKeys[k] == "day":
                yearMonthDay[d] = yearMonthDay[d] + int(kwargs.get(listWithKeys[k]))

    for d in range(len(hoursMinutesSeconds)):
        for k in range(len(listWithKeys)):
            if d == 0 and listWithKeys[k] == "hours":
                hoursMinutesSeconds[d] = hoursMinutesSeconds[d] + int(kwargs.get(listWithKeys[k]))
            elif d == 1 and listWithKeys[k] == "minutes":
                hoursMinutesSeconds[d] = hoursMinutesSeconds[d] + int(kwargs.get(listWithKeys[k]))
            elif d == 2 and listWithKeys[k] == "seconds":
                hoursMinutesSeconds[d] = hoursMinutesSeconds[d] + int(kwargs.get(listWithKeys[k]))
    dateAndTime = convertListToFormattedTime(date = yearMonthDay, time = hoursMinutesSeconds)
    output = formatTimeToWithinBounds(dateAndTime)
    return output

def convertListToFormattedTime(**kwargs):

    '''
    Converts time and/or date passed as an arg.\n
    Passed arg has to be of type list.\n
    Use 'time = yourVariable' to format yourVariable to 'HH:MM:SS'.\n
    Use 'date = yourVariable' to format yourVariable to 'YYYY-MM-DD'.\n
    '''
    
    listWithKeys = list(kwargs.keys())

    time = ""
    date = ""
    for k in range(len(listWithKeys)):
        if listWithKeys[k] == "date":
            for i in range(len(kwargs.get(listWithKeys[k]))):
                separator = "-"
                if i == len(kwargs.get(listWithKeys[k])) - 1:
                    separator = ""
                date = date + str(kwargs.get(listWithKeys[k])[i]) + separator
        if listWithKeys[k] == "time":
            for i in range(len(kwargs.get(listWithKeys[k]))):
                separator = ":"
                if i == len(kwargs.get(listWithKeys[k])) - 1:
                    separator = ""
                time = time + str(kwargs.get(listWithKeys[k])[i]) + separator

    didTime = False
    didDate = True

    if ":" in time:
        didTime = True

    if "-" in date:
        didDate = True

    if didDate and didTime:
        return date + " " + time
    elif didTime:
        return time
    elif didDate:
        return date

def formatTimeToWithinBounds(dateAndTime):

    '''
    Formats time so the time reasonable.\n
    Arg passed should be in the format 'YYYY-MM-DD HH:MM:SS'.\n
    Arg should be a string.\n
    '''

    splitList = str(dateAndTime).split(" ")
    print(splitList)
    yearMonthDay = getYearMonthDay(splitList[0])
    hoursMinutesSeconds = getHoursMinutesSeconds(splitList[1])

    dateAndTime = [yearMonthDay[0], yearMonthDay[1], yearMonthDay[2], hoursMinutesSeconds[0], hoursMinutesSeconds[1], hoursMinutesSeconds[2]]
    maxBound = [9999, 12, monthrange(dateAndTime[0], dateAndTime[1])[1], 24, 60, 60]

    #print(maxBound)

    for i in range(len(dateAndTime) - 1, -1, -1):
        try:
        #print(i)
            while dateAndTime[i] > maxBound[i]:
                if dateAndTime[i] > maxBound[i]:
                    dateAndTime[i] = dateAndTime[i] - maxBound[i]
                    dateAndTime[i - 1] = dateAndTime[i - 1] + 1
        except Exception as e:
            print(e)

    amountOfSegmentsInDate = 3
    date = ""
    for i in range(amountOfSegmentsInDate):
        seperator = "-"
        if i == amountOfSegmentsInDate - 1:
            seperator = ""
        date = date + str(dateAndTime[i]) + seperator

    amountOfSegmentsInTime = 3
    time = ""
    stop = amountOfSegmentsInDate + amountOfSegmentsInTime
    for i in range(amountOfSegmentsInDate, stop, 1):
        seperator = ":"
        if i == stop - 1:
            seperator = ""
        time = time + str(dateAndTime[i]) + seperator

    return date + " " + time


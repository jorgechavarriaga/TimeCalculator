def add_time(start, duration, day=None):
    daysLater = 0
    periodsLater = 0
    startingTime, period = start.split()  
    hour, minute = startingTime.split(':')   
    hourStarting = int(hour)
    minuteStarting = int(minute)
    durationHour, durationMinute = duration.split(':') 
    hourEnd = int(durationHour)
    minuteEnd = int(durationMinute)  
    startingAmOrPm = period

    addMinutes = minuteStarting + minuteEnd  
    addHours = hourStarting + hourEnd  

    if (addMinutes > 59):   
        addMinutes -= 60
        addHours += 1

    addHoursPeriod = addHours

    while addHours > 12:
        addHours -= 12

    while addHoursPeriod > 11:   
        addHoursPeriod -= 12
        if period == "AM":
            period = "PM" 
        else:
            period = "AM"
        periodsLater += 1

    if (periodsLater % 2 != 0):
        if startingAmOrPm == "PM":
            periodsLater += 1
        else:
            periodsLater -= 1

    daysLater = periodsLater / 2

    newHourTimeStr = str(addHours)
    newMinutesTimeStr = str(addMinutes).zfill(2)
    newTime =  newHourTimeStr + ":" + newMinutesTimeStr + " " + period

    daysOfWeek = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

    if (day):
        indexDay = daysOfWeek.index(day.title())
        newIndexDay = int((indexDay + daysLater) % 7)
        newTime += ", " + daysOfWeek[newIndexDay]

    if (daysLater == 1):   
        newTime += " (next day)"

    daysLaterStr = str(int(daysLater))
    if (daysLater > 1):  
        newTime += " (" + daysLaterStr + " days later)"

    return newTime   

print(add_time("3:30 PM", "2:12"));
print(add_time("11:55 AM", "3:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("11:40 AM", "0:25"))
print(add_time("11:40 AM", "0:25"))
print(add_time("8:16 PM", "466:02"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))
print(add_time("11:09 AM", "86400:02", "friday"))

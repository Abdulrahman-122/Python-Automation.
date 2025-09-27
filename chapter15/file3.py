# Pausing Until a specific Date:
# using : time.sleep() to pause a program at specific date

import datetime, time

# datenow=datetime.datetime.now()
# about100days=datetime.timedelta(days=100)
# while datenow+about100days<datetime.datetime(2026,12,12,10):
#     time.sleep(1)
#
# when you get to that time  (2026,12,12)
# the while loop stop
#

#
# convertint datetime objects into strings:
# as the epoch timestamp and datetime object aren't comfortable for user eye
# so we use strftime()(string format time) to convert time object to a string
# Directives of strftime()
# 1.%Y  stands for year for century
# 2.%y             year without century (00:99)
# 3.%m             Month as a decimal number (01:12)
# 4.%B             Full month name (January)
# 5.%b             Abbreviated month name (jan)
# 6.%d             Day of month (01:31)
# 7.%j             Day of the Year (001:366)
# 8 %w             Day of the week (0:6)
# 9.%A             fullweekday name (Monday)
# 10.%a            Abbreviated weekday name : Mon
# 11.%H            Hour (24 hour clock)(00:23)
# 12.%I            Hour(12 hour clock)(00:12)
# 13.%M            Minute (00:59)
# 14.%S            second(00:59)
# 15.%P            'AM or Pm
# %%                literal "%" character


# pass to strftime()
# a custom format string with formatting directives with slashes and colons.....
# the strftime will return the datatime object's info as a formated string
import datetime

oct = datetime.datetime(2025, 10, 13, 11, 22, 22)
formattedstring = oct.strftime("%y:%B:%d:%j:%w:%A")
print(formattedstring)
for_str2 = oct.strftime("%a:%I:%M:%S:%p:%%")
print(for_str2)

# Converting strings into datetime Objects:
# to convert from this to this : use strptime(string,parse)
# parse -> the same directives that like  the string to make strptime( ) understand that string and convert it to datetime
import datetime

act = datetime.datetime(2025, 10, 22, 11, 12, 22, 1)
formattedstr = act.strftime("%A %H:%M:%S %p %%")
print(formattedstr)
formated_datetime = datetime.datetime.strptime("Oct 21 ,2025", "%b %d ,%Y")
print(formated_datetime)
formatted_date2 = datetime.datetime.strptime(formattedstr, "%A %H:%M:%S %p %%")
print(formatted_date2)
formatted_date3 = datetime.datetime.strptime("November 11:12:12", "%B %I:%M:%S")
print(formatted_date3)
Update_form_date3=formatted_date3.replace(year=2000)
print(Update_form_date3)   # here you will see the change
print(formatted_date3)     # here no change still the same year(1900)
#strptime(string,customformatstring)

#Review of Python's time functions;
# 
# a Unix epoch timestamp -> return a number of seconds from 12 Am on January 1 1970
# datetime object of datetime module has (integers stored in year , month,day,hour,minute,second)
# 
# timedelta object represent a specific duration rather than specific moment
# 
# Review on time functions:
# time.time() -> returns an epoch timestamp float value of the current moment
# time.stop(sec) -> pause a program for the amount of seconds
# datetime.datetime(year,month,day,hour,moment,sec) -> return a date object (if no arguments of these not have a value it will return a 0 in it's place)
# datetime.datetime.now() return the datetime object for the current moment
# datetime.datetime.fromtimestamp(epoch) return a datetime object from the epoch timestamb
# datetime.timedelta(week,days,hours,minutes,seconds,milliseconds,microseconds) ->  return a timedelta object (represent the time duration)
# 
# timedeltaobject.total_seconds()-> return the time in  seconds for the timedelta object represent
# note: timedelta doesn't take (month or year)
# strftime(format)-> return a custom string format from the datetime object
# strptime(string,format)-> return a datetime format from the string (format should be represent string)




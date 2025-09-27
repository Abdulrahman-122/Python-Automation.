# The datatime Module:
# it's better for getting Unix epoch timestamp
# to display date in a convenient way
# to do arithmatics with dates
# to know what date was 205 days ago or what date is 12 days from now
# use datetime module
#

import datetime

dt = datetime.datetime.now()
print(dt.year + dt.month + dt.day)
print(dt.hour, dt.minute, dt.second)
print(dt)
# datetime attributes
# .now -> contain on .year ,.month,.day,.hour,.minute,.second


# unix epoch timestamp can be converted to a datatime
# by using: datatime.datatime.fromtimestamp()-> data and time can be converted from local time zone
import time

print(
    datetime.datetime.fromtimestamp(10000000)
)  # return datetime object for the moment 1000000 seconds after the unix epoch
print(
    datetime.datetime.fromtimestamp(time.time())
)  # return datetime object for the time now after the  unix epoch time


# datetime.now()==datetime.fromtimestamp(time.time()) they give you the same datetime
#


# # You can use comparison operators with datetime objects
# dt1 = datetime.datetime(2023, 1, 1)
# dt2 = datetime.datetime(2024, 1, 1)
# print(dt1 < dt2)   # True
# print(dt1 == dt2)  # False
# print(dt1 > dt2)   # False
# dt1=datetime.datetime(2025,6,12)
# dt2=datetime.datetime(2025,6,12)
# print(dt1==dt2)
# print(dt1>dt2)

# the timedelta Data Type:
# timedelta -> represent duration of time rather than a moment in time
import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds)
print(delta.total_seconds())
print(str(delta))

# total_seconds() will return the duration in number of seconds
# passing  a delta object to a string -> return a nicely formatted of time
#
# We use timedelta with datetime to perform date and time arithmetic.
# For example, you can add or subtract a timedelta from a datetime object to get a new date/time.
dt_now = datetime.datetime.now()
dt_future = dt_now + datetime.timedelta(days=5)
dt_past = dt_now - datetime.timedelta(days=10)
print("5 days from now:", dt_future)
print("10 days ago:", dt_past)
# Another useful concept is that timedelta can be used to calculate the difference between two datetime objects.
# The result of subtracting one datetime from another is a timedelta object representing the duration between them.

dt1 = datetime.datetime(2024, 6, 1, 12, 0, 0)
dt2 = datetime.datetime(2024, 6, 15, 18, 30, 0)
difference = dt2 - dt1
print("Difference between dt2 and dt1:", difference)
print("Days:", difference.days)
print("Total seconds:", difference.total_seconds())
# timedelta
delta = datetime.timedelta(days=11, hours=10, minutes=12, seconds=2)
print(str(delta))
print(
    delta.total_seconds()
)  # return the time in second (11days,10 hours , 12min, 2 second=987122.0)

# Doing arithmatic opearations on time
import datetime

dt = datetime.datetime.now()  # get dateobject for now
thousand_days = datetime.timedelta(days=1000)  # get dateobject for 100 days
print(thousand_days + dt)  # add both of dateobject


# using operators :* / , - ,+
import datetime

oct2025 = datetime.datetime(2025, 12, 12, 10, 20, 0)
abouttheryyears = datetime.timedelta(days=365 * 30)
print(str(abouttheryyears))
print(oct2025 + abouttheryyears)
print(oct2025 + (10 * abouttheryyears))
print(oct2025 - (10 * abouttheryyears))

# Keeping Time ,Scheduling Tasks, And Launching Programs:
# Are you Ask yourself can I make a program that can do things for me while sleeping
# and make things like running the program at 5 am or at midnight each day
# all of these can be done using  supprocess and threading modules
#
# the time module:
# your pc has  a time zone and time .
# time module allow you to read the time for the current time
# time.time() or time.sleep()
# the time.time():
#
import time

print(time.time())
# Unix epoch;
# computers measure time starting from a fixed point
# at : junuary 1,1970 at 00:00:00 (UTC) it's called unix epoch
# time.time()
# tells you what's the second that passed from that time untill right now
# why this useful:
# as it give you the same time whenever you was  or your time zone
# programmers used it to :
# measure durations
# timestaps in logs
# Scheduling in timers
#
# you can use timestamp epoch to calculate the time that program take to do it's task
# by putting it into the begaining and at the end then subtract that
# ex:
import time, sys, cProfile

sys.set_int_max_str_digits(
    1000_000_000
)  # this line put the limit number the program needs to run or print a specific number to the screen


# def Calcprod():
#     product = 1
#     for i in range(1, 10):
#         product = product * i
#     return product


# starttime = time.time()
# prod = Calcprod()
# endtime = time.time()
# print(f"The result is {prod} digit long")
# print(f"It takes:{starttime-endtime} seconds to finish this task.")
# cProfile.run( "Calcprod()")


# to see the time that function take use:
# and diagnostic this function : use
# Cprofile module
# by: Cprofile.run('functionname(arg)')  then it will analyse it as you saw above.

# time.sleep() function:
# used to pause the program for a number of seconds
#
# import time
# for i in range(3):
#     print('tick')
#     time.sleep(1)
#     print('tock')
#     time.sleep(1)

# time.sleep(30)
# for i in range(30):
#     time.sleep(1)
#     print("vs", end="")
#
#
# press CTRL+c to keyboardInterrupt


# Rounding numbers:
# round(float,numberofrounds)
# if you want to round a float num with many digits after the decimal point
# just determine the number of rounds
# if you didn't python will take the nearst to the whole integer
import time

now = time.time()
print(now)
print(round(now, 2))
print(round(now, 4))
print(round(now))


#
#
#
#

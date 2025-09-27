# Multithreading:
# in original programs:you will have a single thread(it's like a finger)
# that walk over the lines of code in a flow control statement
# but if you delay your program a duration using: time.stop(sec)
# the program will stop at this delay as you have just single thread
# but if you want to make a many threading to work many parts of your program at the same time
# you will use : threading module
#
import datetime, time

oct = datetime.datetime(2025, 12, 14, 0, 0, 0)
# while datetime.datetime.now() < oct:
#     time.sleep(1)
# print('Now program starting on  Decamber 2025 ')

# now to make a thread object:
# call: threading.thread(target=somthing you want to run(function,....)) this will return a thread object
# then call: threadobj.start() which mean that (run this thread)
# note: this thread is separated from the original thread of program
#
# import datetime, time, threading

# print("Start's of program.")


# def TakeANaP():
#     time.sleep(5)
#     date = datetime.datetime.now()
#     print(f"The time now ={date}")


# threadobj = threading.Thread(target=TakeANaP)
# threadobj.start()
# print("End of program.")


# As you see :
# the program:will start with the original thread (run first print(start...) then go to print(end...))
# then go to the second thread (at it was delayed by 5 minutes but if it was not -> then the second thread will run first then return to the original one )
# Note : we enter the target = functionname(TakeANap)  not  the return value from fun(TAkeANaP())
# this is as you want to pass function itself as argument not it's return value
# two threads
# first (start with first print) and (end with second print)
# second(start with function  and end after the function return value)
#


# Passing arguments to the thread's Target Function:
# always pass your arguments to any function in the thread using
# args,kwargs
print("Dogs", "Cats", "Lions", "Frogs", sep="$")  # now this run in the original thread
# to make a new thread and run it
import threading
print('before thread')
threadObj = threading.Thread(
    # target=print, args=["Dogs", "Cats", "Lions", "Tigers"], kwargs={"sep": "$"}
    target=print("Dogs", "Cats", "Lions", "Frogs", sep="#")
)
threadObj.start()
print('After thread')

# now : we make a new thread and attach it to a new function
# print
# and used args,kwargs
# if you used target=print('dogs','cats',sep='$') this is wrong way to use it as you try to taget the None value of print not itself even it's work 
#but the value that passed to the target is None
#


#Concurrency Issues:
#
#it's because multiple threads read and write the same variables
#this cause threads to trip over each other
#and this append a Concurrency Issues
#so to avoid this 
#makesure that the target function only use the local variables in that functions
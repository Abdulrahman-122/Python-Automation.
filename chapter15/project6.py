# : Simple Countdown Program
# it's countdown that plays an alarm at the end of the countdown
# how it works:
# count down from 60
# play a sound file when the countdown reaches zero
# this mean:
# using time.sleep() to pause for 1 second in between displaying each number
# in the countdown
# call subprocess.popen() to open  the sound file 
# How this program works;
# in command line of the VSC write:
# py project6.py N             where N is the number of countdown you want to make

#py project6.py 60


# import time,subprocess,sys

# timeleft=int(''.join(sys.argv[1:]))
# while timeleft>0:
#     print(timeleft)
#     time.sleep(1)
#     timeleft-=1
# subprocess.Popen(['start','alarm.wav'],shell=True)



#you can change this alarm to a text file with text='Countdown done'
# or using webbrowser.open(website you want to open)
# or change this alarm to another thing


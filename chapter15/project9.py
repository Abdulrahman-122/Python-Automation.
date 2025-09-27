# Prettified Stopwatch
# add some addition on project1
# use ljust() and rjust() to make it look this:
# Lap # 1: 3.56 ( 3.56)
# Lap # 2: 8.63 ( 5.07)
# Lap # 3: 17.68 ( 9.05)
# Lap # 4: 19.11 ( 1.43)
# and then
# copy the output to the clipboard
# in order to paste it to a file or an email

import time, datetime, sys, pyperclip


print("StopWatch")
print("Starting")
print("Click enter to start stop watch:")
print("Click enter to go to second lap .....")
print("Click Ctrl+c to stop stop watch")
input()
start_time = time.time()
lasttime = start_time
lapNumber = 1
laps=[]
try:
    while True:
        input()
        laptime = round(time.time() - lasttime, 2)
        total_time = round(time.time() - start_time, 2)
        print(
            f"lap #{str(lapNumber).rjust(2)}: {str(laptime).rjust(4).ljust(2)} ({str(total_time).rjust(6)})",
            end="",
        )
        lapoutput=str(f"lap #{str(lapNumber).rjust(2)}: {str(laptime).rjust(4).ljust(2)} ({str(total_time).rjust(6)})")
        laps.append(lapoutput)
        lapNumber += 1
        lasttime = time.time()
except KeyboardInterrupt:
    print("Stop")
result='Your Laps:\n'
result+="\n".join(laps)
pyperclip.copy(result)
print('Copy your laps to pyperclip correctly')
print('Now you put result in any email or file using clipboard.')
print("Done")


#
#

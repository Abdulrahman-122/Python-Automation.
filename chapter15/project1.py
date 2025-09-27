# Super Stopwatch:
# this program doing :
# start timing when the script runs.
# hit enter to record (laps)->lap1,lap2,....
# see how much time passed in total and in that lap.
# Quit anytime with Ctrl+C.

# How it works:
# use time.time()  (start timestamp)
# wait for user input(each time you press enter->the program records a lap)
# Keep a lap counter (start with lap=1, every Enter pressed add 1)
# Calculates times:
# laptime=currenttime-time at start of previous lap
# Total time=current time -timewhen the program stated
# print results (lap #num: laptime(total,totaltime))
# by make ctrl+c -> exit from program.
#
#
import time

print(
    "press Enter to begin\nAfterwords print Enter to 'Click' the stopwatch\nPress Ctrl-C to Quit."
)
input()
print("Started.")
starttime = time.time()
lasttime = starttime
lap = 1
try:
    while True:
        input()  # if you press Enter the lap will doubled and print('with detailed to the screen')
        time_lap = round(time.time() - lasttime, 2)
        total_time = round(time.time() - starttime, 2)
        print(f"lap#{lap}:time_lap:{time_lap}(totaltime={total_time}).", end="")
        lap += 1
        lasttime = time.time()
except KeyboardInterrupt:
    print("Done.")

# Lap:
# a one segment of time you want to measure
# if you in a race :
# if you click stopwatch:
# the lap start
# then when you click stopwatch at the end of the race
# you click the stopwatch ; to end the lap
# then you see the time you take to finish the lap(race)

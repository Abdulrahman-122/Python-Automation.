# Looking Busy
# many instant messaging determine whether you are idle or away from your computer
# by detecting a lack of mouse movement over some period of time (ten minute)
# you want to sneak away from your computer and don't want other to know that your account in idle state
# so :
# write a script to nudge your mouse cusor slightly every ten seconds
# the nudge is small enoght and that doesn't prevent you from doing anything on the computer while your script working

# steps:
# use pyautogui
# use FAILSAFE =TRUE
# use while loop :
# use moveRel(x,y,duration=.25)
# time sleep()
# moveRel(x,y,duration=.25)



import pyautogui,time

pyautogui.FAILSAFE=True
pyautogui.PAUSE=1        #stop as you calling each pyautogui for 1 second

while True:
    pyautogui.moveRel(100,0,duration=.25)

    pyautogui.moveRel(-100,0,duration=.25)
    time.sleep(60*10)  #make it wait 10 min then move to the website again

    

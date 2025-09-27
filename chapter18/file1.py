# Controlling The KeyBoard And Mouse with GUI Automation
# think of python scripts you do to make automation for things on your pc
# all of these you control it by the mouse and keyboard and you should be doing it every time
# now : there are  another thing of autmation called:GUI(Graphical user interface automation)
# which is like a robotic arm that make these automation and control mouse and keyboard without you
# and this is important for mindless clicking or filling out of foms
#
# we will use: pyautogui module to make simulation mouse movements
# button clicks
# scrolling the mouse wheel
#
# we will cover a few on pyautogui -> to read more go to
# http://pyautogui.readthedocs.org/.
#
# with problems with GUI robotics like you can't return your control
# steps:
# log out of your pc by : ctrl+Alt+del
# or
# make fail-safe features at your program
# and using pyautogui.pause=1.5 to pause any pyautogui in your program for 1.5 seconds and move the mouse will raise .failsafeException
#
#

import pyautogui

pyautogui.PAUSE = 1  # pause 1 second after each function call
pyautogui.FAILSAFE = True #enabling fail-safe feature to protect my system

# Controlling Mouse Movement:
# the moving of mouse in your program
# track the x,y coordinate of your pc
# x -> increase from 0 to max width of your screen
# y-> increase from 0 to max height of your screen
# if your screen's resolution is 1920*1080
# this mean the max width = 1919
# the max height=1079
# as we start from origin (0,0)
# as we subtract 1 from resolution
#
# to see your screen size:
import pyautogui

print(pyautogui.size())  # return a tuble with (x,y)
width, height = pyautogui.size()
print(width)
print(height)l

#my system resolution is : 1920*1080 

#Moving the Mouse:
#use pyautogui.moveto(x,y,duration=numberofseconds)
#here duration -> control the time that mouse will move to the postion yoi specify by x,y
# it's an optional so the default value of it 0 mean the mouse will move instantly

# 
# 
# import pyautogui
# for i in range(10):
#     pyautogui.moveTo(100,100,duration=.25)
#     pyautogui.moveTo(200,100,duration=.25)
#     pyautogui.moveTo(200,200,duration=.25)
#     pyautogui.moveTo(100,200,duration=.25)
#this will move the mouse in a square pattern
# if you didn't use duration this will make it very fast and you will not see the mothion


# you can make the mouse move whereever it was on the screen
#using moveRel(x,y,duration)
#if you moved to right or bottom -> use positive value
# ~~~~~~~~~~~~~  left or top  -> use negative value
# import pyautogui
# for i in range(10):
    # pyautogui.moveRel(100,0,duration=.25) #from your position(mouse move from it's position on the sceen) move 100 to right
    # pyautogui.moveRel(0,100,duration=.25) # from x=100 make it 0 as it was the refrence then move to bottom 100
    # pyautogui.moveRel(-100,0,duration=.25) # regard the y is the reference than move 100 to left by neg sign
    # pyautogui.moveRel(0,-100,duration=.25) # regard the x is the ref then move 100 to top by neg sign
# Actually, moveRel always uses the current mouse position(new position of mouse) as the reference (you don’t reset anything manually).

# Getting the mouse Position:
# 
# to determine where your mouse on the screen (it's place)
# use; pyautogui.position()  return  a tuple with x,y of the mouse position
# 
import pyautogui

print(pyautogui.position())


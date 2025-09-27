# Controlling Mouse Interaction:
# let's scrolling , dragging
# clicking the Mouse:
# to click the mouse :
# use:  pyautogui.click() -> click the mouse by default click left button
# pass the x and y coordinates and optional using which mouse button to use
# with the button keyword argument : button='left or right or middle'
# 1756,16
# 39 57
# 29 303

import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# # pyautogui.click((1756, 16), button="left")
# pyautogui.click((39, 57), button="left")
# pyautogui.click((29, 303), button="left")

# Dragging the Mouse:
# means you move mouse by holding any button of it
# you can dragging files between folders by dragging the folder icons
# pyautogui has -> .dragto() or dragRel() which is dragging mouse to the location you want
# or relative to the current location
# .dragTo()==moveTo() and .dragRel()==moveRel()
# they take x,y ,duration of time
# to try these methods try : graphics-drawing application
# like paint on windows
#
# in the begaining of the program I will put 5 sec to expliot it and go to the paint program then choose the pencil or brush tool
#
# make program clicked to make focus window on graphics-drawing app(paint)
# then  use while loop
# and use moveRel or dragRel to move the cursor to the distance you want
#
#
#
#
#
#

import pyautogui, time

# time.sleep(10)
# distance=200
# while distance>0:
#     pyautogui.dragRel(distance,0,duration=.25)
#     distance=distance-5
#     pyautogui.dragRel(0,distance,duration=.25)
#     pyautogui.dragRel(-distance,0,duration=.25)
#     distance=distance-5
#     pyautogui.dragRel(0,-distance,duration=.25)
# print('Done')

# Scrolling the Mouse:
# to scroll the mouse up or down on the page use : scroll() if you give it positive value-> it will scroll up then back to the current position
# if you pass it negative value -> it will scroll down then back it the current position
# pyautogui.scroll(2000)  
# pyautogui.scroll(-2000)

#here we want to use write a program 
#to copy of number say 200 number in 200 lines
#into the pyperclip then pasting them in a new file
#and then make pyautogui.scroll() scroll through them.
#to see nums into the file and the nums you pas

# import pyperclip,pyautogui,time

# numbers=''
# for i in range(200):
#     numbers+=f'Number:{i} '+'\n'

# pyperclip.copy(numbers)

# time.sleep(5)
# pyautogui.scroll(10000)   # now if you open the file I pasted after running directly -> pyautogui will scroll up directly after 5sec
# pyautogui.scroll(-10000)
# print('successed operation....')

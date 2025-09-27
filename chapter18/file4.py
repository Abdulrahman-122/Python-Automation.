# Controlling the Keyboard:
# pyautogui has a virtual keypresses to your computer
# which enables  you to fill out forms or enter text into applications
#


# sending a string from the keyboard:
# pyautogui.typewrite()-> sends virtual keypresses to the computer.
# what these keypresses do debends on what windows and text field have focus.
# you may send a click to the text field to ensure its has a focus on it

# let's write a text in editor
# click the field that contain the line + then write the "Hello world!"

# import pyautogui,time
# time.sleep(5)

# pyautogui.click(600, 600)   #make the screen focus to ready for write on it

# pyautogui.typewrite("Hello world!HellHello world!Helloworld!oworld!",.25)
# the second arg of typewrite will be the time that writer will take to write each character in that string you want to write
#Key Names:
# 
# Not all keys are easy to represent with single text characters
# ex: how do you represent shift or left arrow key as a single character
# these keywords are represented in short string values
# esc for ESC key and enter for ENTER key
# import pyautogui,time
# time.sleep(5)
# pyautogui.click((600,600))
# pyautogui.typewrite(['a','b','left','left','X','Y'],.25)
# left key will move the keyboard cursor

#use: pyaytigui.KEYBOARD_KEYS() uses all possible key strings that pyautogui will accept
# shift -> refers to the left shift key  == shiftleft
# also ctrl and alt, win -> refers to the left side key.
# 

import pyautogui,time
# time.sleep(5)
# pyautogui.click((600,600))
# pyautogui.typewrite(['a','b','c','d'],.24)
# pyautogui.typewrite("Abdulrahman Qasim",.25)
# pyautogui.typewrite(['A','B','D','O','QASIM'],.25)
# pyautogui.typewrite('enter')
# pyautogui.typewrite(['A','B','D','enter','O'],.25)


# Pressing and Releasing the Keyboard:
# mouseDown() and mouseUp(),pyautogui.keyDown(),pyautogui.keyUp()->will send virtual keypresses and releases to the computer
# they passed a keyboard key string
# also  you can use pyautogui.press() which calls both of these functions to make a complete keypress
# pyautogui.press('4') uses to type a string
import pyautogui
# pyautogui.keyDown('shift')
# pyautogui.press('4')
# pyautogui.keyUp('shift')


# HotKey combinations:
# it's a shortcut and a combination of keypresses to invoke some applications
# ex: ctrl+c for copy 
import pyautogui
pyautogui.click((2000,600))
pyautogui.keyDown('ctrl')
pyautogui.keyDown('v')
pyautogui.keyUp('v')
pyautogui.keyUp('ctrl')

# Review on the pyautogui functions:
# moveTo(x,y) move the mouse cursor to the x ,y coordinates
# moveRel(xoffset,yoffset) ->moves the mouse the cursor relative it's current position
# dragto(x,y) -> Moves the mouse cursor while the left button is held down
# dragRel(offX,offy)-> moves the mouse cursor relative to it's current position while the left button is held down
# click(x,y,button) -> simulates a click (left button by default)
# rightClick()-> simulates a right button click
# middleClick()-> simulates a middle button click
# doubleClick()-> simulates a double left button click
# mouseDown(x,y,button)-> simulate the mouse down at the given button at  x,y
# mouseUp(x,y,button)->simulates releasing  the given button at x,y coordinates
# scroll(units) -> simulates the scroll wheel a positive arg scrolls up , a a negative arg scrolls down
# typewrite(message) -> types the characters in the given message string 
# typewrite([key1,key2,key3])-> types the given keyboard key strings
# press(key)=>presses the given keyboard string
# keyDown(key)-> simulates pressing down the given keyboard key
# keyUp(key)-> simulates releasing the given keyboard key
# hotjey([key1,key2,key3])->simulates pressing down keyboard key strings down in order and then releasing them in reverse order
# screenshot()-> returns an image object
# 
# 
# 
# 
# 
# 
# 
# 
# 

# Working with Screen:
# you can create an image file based on the current content of the screen
# by using pyautogui features
# these functions can  return a pillow object file about the current appearance of the screen
#
# How to Get a screenshot:
# using pyautogui.screenshot() to bring an image object now this object you can apply on it all methods you take in chapter 17
# import pyautogui
# im=pyautogui.screenshot()   #make an Image object
# print(im.getpixel((0,0)))
# print(im.getpixel((100,199)))    # as you know getpixel take x,y of the pixel you want to bring it's color  then it return a tuple of RGB value and fourth value not found as the screenshot has fully opaque
# im.save('screen1.png')

# Analyzing the screenshot:
# as you want to click a button on a screen
# so you may make a GUI automation that doing this for you
# but if you pass to it the wrong position click() may click on another thing  to delete and it's may be unsaved yet so
# to avoid all of these we can check the color of this button first if yes  okay finish the work
# we use: pyautogui.pixelMatchesColor(x,y,(RGB))
# it takes 3 values:x,y coordiantes of this button or place to check
# (RGB) color of this place you want to check
# it's return true -> so this color of this place is correct
# it can return False -> if color is not exact what this function return
# let's check these two coordinates
# 1829 27
# 1853 55
#

import pyautogui

# im = pyautogui.screenshot()

# print(im.getpixel((1829, 27)))
# print(im.getpixel((1853, 55)))

# tup1 = (24, 24, 24)
# tup2 = (24, 24, 24)

# first = pyautogui.pixelMatchesColor(1829, 27, tup1)
# second = pyautogui.pixelMatchesColor(1853, 55, tup2)

# if first:
#     pyautogui.click(1829,27)
# else:
#     print('The color doesn\'t match this pixel!!')
# if second:
#     pyautogui.click(1853,55)
# else:
#     print('The color doesn\'t match this pixel!!')


# Image Recognition:
# if you don't know where pyautogui should click
# we will convert to image recognition
# pyautogui will look at the screen by comparing it with an image you provide.
# you take a screenshot of the button you want
# then you it to pyautogui
# pyautogui scans the screen to find where the image appears
# use:
# pyautogui.locateonScreen(image)
# if it finds the images it gives you a tuple of 4 nums(left,top,width,height)
# left -> x coordinate of top-left corner
# top -> y-coordinate of the top-left corner
# width-> width of the found area
# height-> height of the found area
# if image not found on the screen -> locateonscreen() will return a None
# the image on the screen must match the provided image perfectly in ordered to be recognized
#
# if the image found on several places on the screen
# locateonscreen() will return a Generator object
# then it will be passed to a list() to return a list of fourinteger tuples
# one tuple for each location that represent each image which is more than one
# each of four integer tuple represent an area on the screen
# if your area is just found one time on the screen -> and then you put it's object inside a list
# it will return a list of four values
#
# once you have the area
# so to bring the tuble of it's center(left,top)
# use .center with: pyautogui.center((tuple))
# then you can pass the the tuple of the center to the click () to click on this image


#
# import time

# button = pyautogui.locateOnScreen("screen3.png")
# time.sleep(5)
# print(button)
# center = pyautogui.center((995, 74, 818, 941))

# pyautogui.click((1404, 544))
# print("Done.")

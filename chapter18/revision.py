import pyautogui, time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

# width, height = pyautogui.size()
# print(width, height)

# for i in range(10):
#     pyautogui.moveTo(100,100,duration=.25)
#     pyautogui.moveTo(200,100,duration=.25)
#     pyautogui.moveTo(200,200,duration=.25)
#     pyautogui.moveTo(100,200,duration=.25)

# for i in range(10):
#     pyautogui.moveRel(100,0,duration=.25)
#     pyautogui.moveRel(0,100,duration=.25)
#     pyautogui.moveRel(-100,0,duration=.25)
#     pyautogui.moveRel(0,-100,duration=.25)

# print(pyautogui.position())

# pyautogui.click((1900, 10), button="left")
# pyautogui.click((1900, 10), button="right")
# pyautogui.click((1900, 10), button="middle")

# for i in range(10):
# pyautogui.dragTo(100,100,duration=.25)    # drag means move mouse with hold a button
# pyautogui.dragTo(200,100,duration=.25)
# pyautogui.dragTo(200,200,duration=.25)
# pyautogui.dragTo(100,200,duration=.25)

# for i in range(10):
#     pyautogui.dragRel(100,0,duration=.25)
#     pyautogui.dragRel(0,100,duration=.25)
#     pyautogui.dragRel(-100,0,duration=.25)
#     pyautogui.dragRel(0,-100,duration=.25)

# time.sleep(10)
# distance=200
# while distance >0:
#     pyautogui.dragRel(distance,0,duration=.25)
#     distance=distance-5
#     pyautogui.dragRel(0,distance,duration=.25)
#     pyautogui.dragRel(-distance,0,duration=.25)
#     distance=distance-5
#     pyautogui.dragRel(0,-distance,duration=.25)
# print('Done..')

# pyautogui.scroll(10000)
# pyautogui.scroll(-10000)

# im = pyautogui.screenshot()
# print(im.getpixel((9,9)))
# print(im.getpixel((199,199)))


# first = pyautogui.pixelMatchesColor(9, 9, (24, 24, 24))
# second = pyautogui.pixelMatchesColor(199, 199, (31, 31, 31))

# if first:
#     print("Yes")

# if second:
#     print("Yeah")

# imageborder = pyautogui.locateOnScreen(
#     'screen7.png'
# )
# time.sleep(20)
# # print(imageborder)

# time.sleep(10)
# pyautogui.click((700,700))
# pyautogui.typewrite('Hello Osame I am very glad as you here thanks for coming I am wish a good day for .',.25)

time.sleep(10)
pyautogui.click((1600,500))
# pyautogui.typewrite(['a','b','d','o','1','2','3','!','@'])
# pyautogui.typewrite(['Hello','enter','world'])
# pyautogui.press('esc')
# pyautogui.keyDown('shift')
# pyautogui.press('a')
# pyautogui.keyUp('shift')
# pyautogui.typewrite(['a','tab','b'])
# pyautogui.typewrite('Hello')
# pyautogui.press('backspace')
# pyautogui.press('pagedown')
# pyautogui.press('home')
# pyautogui.press('end')

# pyautogui.typewrite(['a','b','left','left','X','Y'])
# pyautogui.typewrite(['a','b','right','right','X','Y'])
# pyautogui.press('f5')    
# pyautogui.press('volumedown')
# pyautogui.press('pause')
# pyautogui.press('capslock')
# pyautogui.press('insert')
# pyautogui.press('printscreen') # make a screenshot 
# pyautogui.press('winleft')

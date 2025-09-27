#Insatant Messanger Bot:
# you want to open a Google talk and open a new chat with yourself if you don't have any friends
# if you have add the friends you want to your Google talk
# then make a google talk +then create the space + then space name 
# then the messanger window will open 
# steps:open Google Talk
# use pyautogui
# use screenshots to guid GUI interaction 
# when the virtual keystrokes aren't being sent.
#then after run the code : open the max window of Google Talk


import pyautogui,time

time.sleep(10)

pyautogui.click((1021,924))
pyautogui.typewrite('Hello How can i benefit from you',.2)
pyautogui.press('enter')
#Where Is the Mouse Right Now?
# we want to move the cursor and bring it's position while its moving
# at hight level
# Display the x,y coordinate of mouse cursor
# update these coordinates as the mouse moves around the screen
# 
# you should do the following;
# call position () to fetch the current position
# erase the previously coordinates by enter \b backspace to the screen
# handle the keyboardInterrupt exception so the user can press ctrl+c to quit
# 
#
#

import pyautogui

pyautogui.PAUSE=1
pyautogui.FAILSAFE=True

print('Press Ctrl-C to quit.')
try:
    while True:
        x,y=pyautogui.position()
        Position=f'X:'+str(x).rjust(4)+'Y:'+' '+str(y).rjust(4)
        print(Position,end='') 
        print('\b'*len(Position),end='',flush=True) 
except KeyboardInterrupt:
    print('\nDone')
       
# we used end in the first print as it make all output at the same line
# in the second print we use '\b' backspace character to erase all the previous output
#by multiply it in the length of output you want to erase 
#then we end with end='' which means  don't go to the next line and without this you can't erase chars
#as you go to the next line each time so we put it to make this
#also we use flush=True -> to show output at the stream (screen) directly not after python store it
#so we use it to fast shown output


# Extending the mouseNow program
# extend project1 to get the RGB tuple of the x,y coordinate of
# any arbitrary coordinates under the cursor
#
import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

print("Press Ctrl-C to quit.")
try:
    while True:
        x, y = pyautogui.position()
        Position = f"X:" + str(x).rjust(4) + " Y:" + " " + str(y).rjust(4)
        pixelcolor = pyautogui.screenshot().getpixel((x, y))
        # Position += "RGB:" + str(pixelcolor)  #if you use this line ->as it is it will return a fourth value with it that represent alpha
        Position+='RGB: ('+str(pixelcolor[0])+', '+str(pixelcolor[1])+', '+str(pixelcolor[2])+' )'
      

        
        print(Position, end="")
        print("\b" * len(Position), end="", flush=True)
except KeyboardInterrupt:
    print("\nDone")

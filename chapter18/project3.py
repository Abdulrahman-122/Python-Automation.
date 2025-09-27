# Automatic Form Filler:
# 
# enter the data into the spreadsheet into the google form
# At a high level -> what's your program should do:
# click the first text field of the form
# move through the form typing information in each field
# click the submit button
# Repeat the process with the next set of data
# 
# so you will use:
# pyautogui.click() to click each field and submit button
# pyautogui.typewrite() to write text into the fields
# handle the keyboardinterrrupt so; the user press ctrl+c to quit
#steps:
# click the Name field by determine the coordinates the field input of the first field
# (use the click then tab to go to the next field)
# 1. then type the name then press tab
# 2.type the greatest fear then press tab
# 3.press the keydown the correct number of times to select the wizered power source
# once for wand,twice for amulet,three times for crystal ball , four times for money then press tab
# 4,press the right arrow key to select the answer to RoboCop question
#press it once for 2 or twice for 3 or three for 4 or four for 5
# then press tab
# 5.type an additional comment then press tab
# 6.press the enter key to submit button
# after the submitting -> browser will take you to a page where you will click the link to return to the form page
# this is the link for google form;  https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform

#NOte that : we will depend on the project 1 to find the coordinates of the first field.
# the coordinates of firstfiled:

# import pyautogui

# try:
#         pyautogui.click((1120,335))
#         pyautogui.typewrite('Abdulrahman Ayman Qasim')
#         pyautogui.press('tab')
#         pyautogui.typewrite('My greatet fear is to die without good work that serves our humanity.')
#         pyautogui.press('tab')
#         pyautogui.press('down',presses=4)
#         pyautogui.press('tab')
#         pyautogui.press('right',presses=2)
#         pyautogui.press('tab')
#         pyautogui.typewrite('This form give me a nice idea it thank you')
#         pyautogui.press('tab')
#         pyautogui.press('enter')
#         print('Done the first image')
# except:
#     print('Something happend ......')
import pyautogui,time

namefield=(690,555)

submitbutton=(622,799)
anotherlink=(695,344)
sumbitbuttoncolor=(130,130,130)
anotherlinkcolor=(255,255,255)



formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 
 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
 {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 
 'comments': 'n/a'},{'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 
 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
 {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 
 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
 ]

pyautogui.PAUSE=.5     #pause for .5 second after call each function

for person in formData:
    print('>>> 5 second pause (Ctrl+C to abort) <<<')
    time.sleep(5)

    # Wait until form is ready
    # while not pyautogui.pixelMatchesColor(submitbutton[0], submitbutton[1], sumbitbuttoncolor):
    #     time.sleep(0.5)

    print(f"Entering {person['name']}...")

    # Name + Fear
    pyautogui.click(namefield)
    pyautogui.typewrite(person['name'] + '\t')
    pyautogui.typewrite(person['fear'] + '\t')

    # Wizard Power
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

    # RoboCop rating
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Comments
    pyautogui.typewrite(person['comments'] + '\t')

    # Submit
    pyautogui.press('enter')
    print('Clicked Submit.')

    # Wait & click "Submit another response"
    time.sleep(5)
    pyautogui.click(anotherlink)
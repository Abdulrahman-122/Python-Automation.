# Launching other Programs from python:
# by using popen() python can start any program on it
# p in popen -> means process
# if you open multiple tap of the same program then each tap has the related process and different from the other one
# each process has a multiple threads but these threads can't write or read another process varaibles
# so : each program has multiple threads but it don't use to run any process
#
# so to open any program
# pass it's file name to popen(filename)
# after importing subprocess
import subprocess

# chrome = subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
# print(chrome)
# anki = subprocess.Popen("C:\Users\hp\AppData\Local\Programs\Anki")
# print(anki)
#
#

# we use poll() -> to ask yourfrind if she's finished running the code you gave her
# poll() return None if the process is still run at the same time is called
# if program has terminated -> return the process integer(exit code)
# precess integer(exit code)-> determine whether the process terminated without error or not
# if process without error -> exitcode =0
# if process with error -> exitcode=1
# wait() -> waiting for friend to finish working on his code before working on yours
# this method will block untill the launched process is terminated
#
# this is useful if you want your program to stop untill the user finishes the other programs
#
# the return value of wait() is the process's integer exit code
#

import subprocess

# chrome=subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')
# print(chrome.poll()==None)     # here return None as the program doesn't work (in opening case)
# print(chrome.wait()) #wait untill the code finsihed or run return 0 to clearify that it's running correctly
# print(chrome.poll()) # return 0 if the program run correctly.


# passing command line Arguments to Popen()
# you can pass command line argument to the process you create with popen()
# you pass a list to popen()
# the first thing in it will be the executable file you want to launch
# all the subsequant strings will be an argument for the program when it starts
# use sys.argv to make this list
# import subprocess , sys
# chrome=subprocess.Popen(sys.argv[1:])
# print(chrome)

# write in command line: py file5.py  path to the App to opon it
# py file5.py C:\Program Files\Google\Chrome\Application\chrome.ex

# open webbrowser programs:
# by using webbrowser.open()  used to open webbrowsers programs from the browser itself
import webbrowser, subprocess

# webbrowser.open('https://www.google.com/youtube')
# webbrowser.open('https://chatgpt.com/c/68c5084d-5610-8330-85da-f873dfd96586')
# subprocess.Popen("D:\c++\Microsoft VS Code\Code.exe")
# webbrowser.open('file1.py')
#


# Opening files with Default Applications
# on windows ->  instead of double click on any file and launch it
# we use  start program that instead double click this file and launch it
import subprocess

# with open("Helle1.txt", "w") as file:
#     file.write("Hello world!")
#     file.close()
# subprocess.Popen(["start", "Helle1.txt"], shell=True)
with open("Hello2.txt", "w") as file:
    file.write("this file is by open in python\n")
    file.write("And will open by subprocess module.(using start program) ")
    file.close()
subprocess.Popen(["start", "Hello2.txt"], shell=True)


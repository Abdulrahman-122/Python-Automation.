# Brute-force Pdf password Breaker:
# you forgitten the password of encrypted files
# and you want to open these files
# but you remember it was a single English word or a many of integers
#
# what you will do to open these files:
# make a program to decrypt these pdf files
# by trying every possible word untill it finds one can works
# Download file called: dictionary.txt from this folder on your pc as it contain on every possible English word
# untill it finds it's work
#
# skills you need+what's the program will doing:
# file-reading skills
# create a list for all words in this file
# loop over each word in this file
# pass this word to the decrypt ()
# if decrypt return 0 -> this mean this false pass
# go to the next pass
# if decrypt returns 1 -> true pass
# then the program should break the encrypt
# print(the hacked password)
# note: you should try all upper and lower case for each word

import os, pypdf, sys
from pypdf import PdfReader

for item in os.walk("D:\python_content\python_Automation_part2\chapter13"):
    files = item[-1]
# print(files)
pdffile = []

for file in files:
    if file.endswith(".pdf"):
        pdffile.append(file)

with open("dictionary.txt", "r") as dictfile:
    content = dictfile.readlines()
    all_words = [item.strip() for item in content]

for file in pdffile:
    reader = PdfReader(file)

    if not reader.is_encrypted:
        print(f"This file {file} is not encrypted.")

    if reader.is_encrypted:
        print("Crack the file....")
        for i, passw in enumerate(all_words):
            if reader.decrypt(passw.upper()):
                print(f"This password : {passw} True")
                print(f"The passw at index: {i}")
                print(f"This password {passw} for this file {file} (save it with you)")
                break

            elif reader.decrypt(passw.lower()):
                print(f"This password : {passw} True")
                print(f"The passw at index: {i}")
                print(f"This password {passw} for this file {file} (save it with you)")
                break

    else:
        print("Couldn't crack the file.")

    print("Do you want to know the password of the next file or not???")
    move = input("(True/False)>>")
    if move == "True":
        continue
    elif move == "False":
        sys.exit()

# snapshot of output
# 
# This file compine.pdf is not encrypted.
# Couldn't crack the file.
# Do you want to know the password of the next file or not???     
# (True/False)>>True
# Crack the file....
# This password : 1234 True
# The passw at index: 45345
# This password 1234 for this file compine_encrypted.pdf (save it 
# with you)
# Do you want to know the password of the next file or not???     
# (True/False)>>False

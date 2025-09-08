#Text Files to spreadsheet:
# write a program to make ;
# several text files say 2 files
# insert these lines into spreadsheet
# where : the content of the first textfile will be in the column A of spreadsheet
# the content of second textfile in the column B of the spreadsheet and so on...
# use:
# readlines() to return a list of strings from the file
# one string from the file per line in the spreadsheet
# for first file : first line in it should be in  row 1 column 1 in the spreadsheet
# the second lien in it should be in row 2 column 1 and so on

import openpyxl
DateF1="""
Abdulrahman Ayman Qasim
22 years old
from Egypt
Computer





"""
with open('file1.txt','w')as file1:
    file1.writelines('')

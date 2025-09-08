# Text Files to spreadsheet:
# write a program to make ;
# several text files say 2 files
# insert these lines into spreadsheet
# where:
# the content of the first textfile will be in the column A of spreadsheet
# the content of second textfile in the column B of the spreadsheet and so on...
# use:
# readlines() to return a list of strings from the file
# one string from the file per line in the spreadsheet
# for first file : first line in it should be in  row 1 column 1 in the spreadsheet
# the second lien in it should be in row 2 column 1 and so on

import openpyxl

DataF1 = """
Abdulrahman Ayman Qasim
22 years old
from Egypt
Computer Engineer 
Muslim
single 
"""
DataF2 = """
Osama Ayman Qasim
15 years old
from Egypt
High School student
Muslim
single
"""
# with open("file1.txt", "+a") as file1:
#     file1.writelines(DataF1)
#     file1.close()
# with open("file2.txt", "+a") as file1:
#     file1.writelines(DataF2)
#     file1.close()

#now append these files to spreadsheet:

wb=openpyxl.Workbook()
sheet=wb.active

file1=open('file1.txt','r')
lines1=file1.readlines()

file2=open('file2.txt','r')
lines2=file2.readlines()

for item in lines1:
   print(item)
# for item in lines2:
#     o=1
#     sheet['B'+str(o)]=item
#     o+=1
# wb.save('Project6.xlsx')

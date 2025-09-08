# import openpyxl

# wb = openpyxl.load_workbook("example.xlsx")
# print("All sheets:", wb.sheetnames)
# first_sheet = wb["Sheet1"]
# print(first_sheet)
# Second_sheet = wb["Sheet2"]
# print(Second_sheet)
# Third_sheet = wb["Sheet3"]
# print(Third_sheet)
# print(first_sheet.title)
# print(Second_sheet.title)
# print(Third_sheet.title)
# another_sheet = wb.active
# print(another_sheet.title)


# EXcel sheet:
#
# openpyxl.load_workbook -> takes filename and return workbook data type
# wb.sheetnames -> return all sheets.
# this workbook data object is an  the EXcel file.
# wb.sheetnames -> return the sheets of the workbook
# wb.active -> return the top sheet when the workbook is opened in Excel.

# Getting Cells from the sheets:
# once you have a worksheet object
# to access the cell object by  name
#
#
#
import openpyxl

wb = openpyxl.load_workbook("duesRecords.xlsx")
sheets = wb.sheetnames
print(sheets)
sh1 = wb["Sheet1"]
print(sh1)
c1 = sh1["A1"]
print(c1.value)
c2 = sh1["A2"]
print(c2.value)
c3 = sh1.cell(row=3, column=1)
print(c3.value)
sh2 = wb["Sheet2"]
print(sh2)
b1 = sh1["B1"]
print(b1.value)
b2 = sh1["B2"]
print(b2.value)
print(f"The {b1.value} of {c2.value} is {b2.value}")
sh2 = wb["Sheet2"]
# c1 = sh2.cell(row=1, column=3)
# print(c1.value)
for i in range(1, 8,2):
    print(i, f"{sh1.cell(row=i,column=1).value}")
for i in range(1, 8,2):
    print(i, f".{sh2.cell(row=i,column=2).value}")
for i in range(1, 8):
    print(i, f"{wb['Sheet1'].cell(row=i,column=3).value}")
for i in range(1, 8):
    print(i, f"{wb['Sheet1'].cell(row=i,column=4).value}")


#
# using a cell method you can write a for loop to loop over the value inside the cell 
# if you want to print the odd columns press 2 in the range method 
# 
#to determine the size of the sheet  
# use:
# max-row,max-column

import openpyxl
wb=openpyxl.load_workbook('duesRecords.xlsx')
sheets=wb.sheetnames
sh1=wb['Sheet1']
print('Heighst row',sh1.max_row)
print('Heighst column')

# 
# 
# 
# 

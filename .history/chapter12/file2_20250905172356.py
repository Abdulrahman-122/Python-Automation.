# Gitting Rows and Culomns from the sheet:
#
# import openpyxl

# wb = openpyxl.load_workbook("duesRecords.xlsx")
# sheet = wb["Sheet1"]
# # print(tuple(sheet["A1":"H7"]))

# wb=openpyxl.load_workbook('duesRecords.xlsx')
# sh1=wb['Sheet1']
# Allcells=sh1['A1':'H7']
# for row_of_cell in Allcells:
# for cellobj in row_of_cell:
#     print(cellobj.coordinate,cellobj.value)
# print('---End of Row----')


#
# we use tuple to visualize the cells object  at the workbook object
#
# as you see the tuple of sheet contain on seven inner tubles
# each tuble represent the obj of each row from the left to the right
# so the objects into each row is the cell objects for each row.
# we use two for loops to print the cells values
# the outer goes for each each row
# the inner goes for each cell row


import openpyxl

wb = openpyxl.load_workbook("duesRecords.xlsx")
sh1 = wb["Sheet1"]
column_b = sh1["B"]
for collobj in column_b:
    print(collobj.value)
column_a = sh1["A"]
for collobj in column_a:
    print(collobj.value)
column_c = sh1["C"]
for collobj in column_c:
    print(collobj.value)

row1 = sh1[1]
for rowobj in row1:
    print(rowobj.value)
row2=sh1[2]
for rowobj in row2:
    print(rowobj.value)
row3=sh1[3]
for rowobj in row3:
    print(rowobj.value)

# each columns or rows attribute => sh1['A'] or sh1[1]
# gives you the inner tubles which represent the inner cellobj
# once you have one tuble represent one row or column
# you can loop over their value
#
#
#to read the cell from a spreadsheet file
#import openpyxl
#call openpyxl.load_workbook(file)
#Get a workbook object
#call .active , .sheetnames , wb['sheetnumber']
#get worksheetobject
#use index (A,B...)for columns or (1,2,3...) for rows or use .cell(row=num , column=num)
#get a cell object
#Read the cell object's value attribute using : .value
#
#

#
# ideas for similar projects:
#
# compare data across multiple rows in a spreadSheets:
#
#
#
# Writing Excel Documents;
#
# Creating and Saving Excel Documents:

import openpyxl

Wb = openpyxl.Workbook()  # create Workbook object
sheet = Wb.active
print(sheet.title)
sheet.title = "sheetone"  # to make title  for the sheet and create sheet + use create_sheet(title='') to create a sheet
print(Wb.sheetnames)
Wb.create_sheet(title="Spsheet1")
Wb.create_sheet(title="Spsheet2")
Wb.create_sheet(title="Spsheet3")
Wb.create_sheet(title="Spsheet4")
print(Wb.sheetnames)
Wb.save(
    "Multiple_spreadsheet.xlsx"
)  # now to fire that New workbook you made to a new spreadsheet
# Save a copy from the spreadsheet to another spreadsheet
openpyxl
wb = openpyxl.load_workbook("duesRecords.xlsx")
sheet = wb.active
print(sheet)
sheet.title = "Spam Spam Spam"
print(wb.active)
wb.save('RecordsDues.xlsx')     #now we change the title and name of original file 
#now the change will be in the copy file not the original with it's new title


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

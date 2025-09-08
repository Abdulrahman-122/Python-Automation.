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
#use index (A,B...)for rows or (1,2,3...) for co
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
#
#
#
#

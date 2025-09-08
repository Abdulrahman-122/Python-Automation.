# Gitting Rows and Culomns from the sheet:
#
import openpyxl

wb = openpyxl.load_workbook("duesRecords.xlsx")
sheet = wb["Sheet1"]
print(tuple(sheet["A1":"C3"]))

wb=openpyxl.load_workbook('duesRecords.xlsx')
Allcells=wb['A1':'C3']
for row_of_cell in Allcells:
    for collobj in row_of_cell:
        print('Data of row:')
        print(collobj.)


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

# Gitting Rows and Culomns from the sheet:
#
import openpyxl

wb = openpyxl.load_workbook("duesRecords.xlsx")
sheet = wb["Sheet1"]
print(tuple(sheet["A1":"H7"]))

wb=openpyxl.load_workbook('duesRecords.xlsx')
sh1=wb['Sheet1']
Allcells=sh1['A1':'H7']
for row_of_cell in Allcells:
    for cellobj in row_of_cell:
        print(cellobj.coordinate,cellobj.value)
    print('---End of Row----')


#
#we use tuple to visualize the cells object  at the workbook object
#
#as you see the tuple of sheet contain on seven inner tubles
#each tuble represent the obj of each row from the left to the right
#s
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

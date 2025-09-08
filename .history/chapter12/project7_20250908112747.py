#write a spreadsheet into a textfile:
#
#
#
#
#
#
import openpyxl
wb=openpyxl.load_workbook('produceSales.xlsx')
sheet=wb.active
for row in range(1,sheet.max_row):
    for col in 
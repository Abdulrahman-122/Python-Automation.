import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
print('All sheets:',wb.sheetname)
import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
print('All sheets:',wb.sheetnames)
first_sheet=wb["Sheet1"]
print(first_sheet)
Second_sheet=wb['']
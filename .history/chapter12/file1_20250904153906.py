import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
# print(type(wb))       
print(wb.get_sheet_names())       # as you know each sheet has columns and rows

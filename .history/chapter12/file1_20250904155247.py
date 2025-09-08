import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
print("All sheets:", wb.sheetnames)
first_sheet = wb["Sheet1"]
print(first_sheet)
Second_sheet = wb["Sheet2"]
print(Second_sheet)
Third_sheet = wb["Sheet3"]
print(Third_sheet)
print(first_sheet.title)
print(Second_sheet.title)
print(Third_sheet.title)
another_sheet = wb.active    
print(another_sheet.title)



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

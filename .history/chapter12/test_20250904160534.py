import openpyxl
wb=openpyxl.load_workbook('example.xlsx')
print('All sheets:',wb.sheetnames)
sheet1=wb['heet1']
sheet2=wb['sheet2']
sheet3=wb['sheet3']
print(sheet1)
print(sheet2)
print(sheet3)
print(sheet1.title)
print(sheet2.title)
print(sheet3.title)
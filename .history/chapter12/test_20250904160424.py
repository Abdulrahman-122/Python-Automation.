import openpyxl
wb=openpyxl.load_workbook('example.xlsx')
print('All sheets:',wb.sheetnames)
sheet1=wb['sheet1']
sheet2=wb[]
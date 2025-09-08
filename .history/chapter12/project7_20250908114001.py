#write a spreadsheet into a textfile:
#
#
#
#
#
#
import openpyxl
wb=openpyxl.load_workbook('duesRecords.xlsx')
sheet=wb.active
lines1=[]
for row in range(1,sheet.max_row):
    for col in range(1,sheet.max_column):
        lines1.append(sheet.cell(row=row,column=col).value)
        print('\n')

file1=open('File7.txt','w')

file1.writelines(lines1)

print('Done')

# columna=[]
# for row in range(1,sheet.max_row):
#     for col in range(1,sheet.max_column):
#         columna.append(sheet['A'+str(row)].value)
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
# for row in range(1,sheet.max_row):
#     for col in range(1,sheet.max_column):
#         lines1.append(sheet.cell(row=row,column=col).value)
#         print('\n')

# file1=open('File7.txt','w')

# file1.writelines(lines1)

# print('Done')

columna=[]
columnb=[]
columnc=[]
for row in range(1,sheet.max_row):
        columna.append(sheet['A'+str(row)].value)
        columnb.append(sheet['B'+str(row)].value)
        columnc.append(sheet['C'+str(row)].value)
# print(columna)
# print(columnb)
# print(columnc)

for item1 in columna:
        for item2 in columnb:
                for item3 in columnc:
                        print(item1+' '+item2+' '+item3)
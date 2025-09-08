# Updating a spreadsheet:
#
# in the project we will do:
# loop over the rows
# if the produce was galaric or celery or lemon-> update the price of them
# so;
# open the excel file
# if the row of produce has a cellvalue called galaric or celery or lemon
# update the price of them in column B
# save the old file to new one (in order to not lose the data inside it )
# import openpyxl

#first solution:mysolution

# wb = openpyxl.load_workbook("produceSales.xlsx")
# print(wb.active)
# print(wb.sheetnames)

# sheet = wb["Sheet"]
# print(sheet.max_row)
# for i in range(1,23758):
#     if sheet.cell(row=i,column=1).value=='Garlic':
#         sheet.cell(row=i,column=2).value=3.07
#     elif sheet.cell(row=i,column=1).value=='Celery':
#         sheet.cell(row=i,column=2).value=1.19
#     elif sheet.cell(row=i,column=1).value=='Lemon':
#         sheet.cell(row=i,column=2).value=1.27
# print('Done.')
# wb.save('UPda_produceSales1.xlsx')

#second-solution(booksolution)
import openpyxl
wb=openpyxl.load_workbook('produceSales.xlsx')
sh=wb['sheet']
Updated_prices={
    'Garlic':3.07,
    'Celery':1.19,
    'Lemon':1.27
}

for rowobj in range(2,sh.max_row+1):
    produce_obj=sh.cell(row=rowobj,column=1)
    produce_item=produce_obj.value
    if produce_item in Updated_prices.keys:
        produce_item=Updated_prices[rowobj]










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

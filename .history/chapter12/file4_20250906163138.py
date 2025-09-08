# Merging and Unmerging Cells:
# to merge a number of cells with each other
# import openpyxl
# wb=openpyxl.Workbook()
# sheet=wb.active
# sheet['A1']='Twelve merged cells with each other.'
# sheet.merge_cells('A1:D3')
# sheet['D5']='Two merged cells'

# wb.save('merge.xlsx')


import openpyxl
wb=openpyxl.load_workbook('merge.xlsx')
sheet=wb.active
sheet.unmerge_cells('A1:D3')
sheet.unmerge_cells('D3:D5')
wb.save('unmerge.xlsx')


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

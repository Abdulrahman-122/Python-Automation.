# Merging and Unmerging Cells:
# to merge a number of cells with each other
import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet['A1']='Twelve merged cells with each other.'
sheet.merge_cells('A1:D3')
sheet['D5']='Two merged cells'

wb.save('')
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

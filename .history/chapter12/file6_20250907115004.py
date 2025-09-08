#
# openpyxl.load_workbook return  workbook object
# sheetnames return sheetnames
# sheet1=wb['Sheet1']
# Actshe=wb.active
# she['C5'].value
# she['C5']=Hello world
# they return integers as number of max_rows and number of max_columns (max_rows, max_columns)
#
import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string

# we use column_index_from_string to get the integer of M
# use get_column_letter to get the string (column name ) from 14
wb = openpyxl.Workbook()
sheet = wb.active
print((sheet["A1":"F1"]))       # here we make a tuple from A1 to F1
#
#wb.save('example.xlsx')
#sheet['A4']='=SUM(A1:A3)'
#use data_only=True in load_Workbook() function
#use : sheet.row_dimension[5].height=100
#sheet.column_dimension['C'].width=0
# 
# freeze_panes : is a attribute used to frozen all the top_left column and up rows to be visible throw all the spreadsheet
# 
# Reference
# Series
# Barchart()
# chart.append()
# sheet.add_chart
# 







# 
# 
# 




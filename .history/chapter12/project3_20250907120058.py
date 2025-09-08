# Multiplication Table Maker
#
#
# the program take N integer from the command and this will determine the size of table
# N*N  ex if you put:4 -> table will be 4*4 and so on
# -------------------------------------------


import openpyxl

wb = openpyxl.Workbook()
wb.create_sheet("Sheet1")
sheet = wb["Sheet1"]


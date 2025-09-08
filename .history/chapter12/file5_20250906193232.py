#Making Barchart contian on Months with Sales and profits:

import openpyxl
from openpyxl.chart import Reference,BarChart

wb=openpyxl.Workbook()
sheet=wb.active

for i in range(1,9):
    sheet['A'+str(i)]=i
    sheet['A']
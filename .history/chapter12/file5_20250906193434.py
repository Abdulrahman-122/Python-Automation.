#Making Barchart contian on Months with Sales and profits:

import openpyxl
from openpyxl.chart import Reference,BarChart

wb=openpyxl.Workbook()
sheet=wb.active

for i in range(1,9):
    sheet['A'+str(i)]=i          # months
    sheet['B'+str(i)]=i*2        # sales
    sheet['C'+str(i)]=i          # profits
ref=Reference(sheet,min_col=2,min_row=1,max_row=8)

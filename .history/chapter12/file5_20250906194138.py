#Making Barchart contian on Months with Sales and profits:

import openpyxl
from openpyxl.chart import Reference,BarChart

wb=openpyxl.Workbook()
sheet=wb.active

for i in range(1,9):
    sheet['A'+str(i)]=i          # months
    sheet['B'+str(i)]=i*2        # sales
    sheet['C'+str(i)]=i          # profits

ref=Reference(sheet,min_col=2, min_row=1 ,max_row=8)       #ref object for sales
cats=Reference(sheet,min_col=3 ,min_row=1 ,max_row=8)
Chart=BarChart()
Chart.title='Sales Vs Profits'
Chart.x_axis.name='Months'
Chart.y_axis.name='Amount'

Chart.add_data(ref,title_from_data=True)
Chart.set_categories(cats)
sheet.add_chart(Chart,)
# Making Barchart contian on Months with Sales and profits:

# import openpyxl
# from openpyxl.chart import Reference,BarChart

# wb=openpyxl.Workbook()
# sheet=wb.active

# for i in range(1,9):
#     sheet['A'+str(i)]=i          # months
#     sheet['B'+str(i)]=i*2        # sales
#     sheet['C'+str(i)]=i          # profits
# sheet['A1']='Months'
# sheet['B1']='Sales'
# sheet['C1']='Profits'
# ref=Reference(sheet,min_col=2,max_col=3,min_row=1 ,max_row=8)
# cats=Reference(sheet,min_col=1 ,min_row=1 ,max_row=8)
# Chart=BarChart()
# Chart.title='Sales Vs Profits'
# Chart.x_axis.name='Months'
# Chart.y_axis.name='Amount'

# Chart.add_data(ref,titles_from_data=True)
# Chart.set_categories(cats)
# sheet.add_chart(Chart,'E5')
# wb.save('Chart2.xlsx')

# Draw a chart with sales on y-axis and months on x-axis
# import openpyxl
# from openpyxl.chart import Reference, BarChart

# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet["A1"] = "Months"
# sheet["B1"] = "Sales"
# for i in range(2, 11):
#     sheet["A" + str(i)] = i
#     sheet["B" + str(i)] = i * 3

# ref = Reference(sheet, min_col=1,max_col=2, min_row=1, max_row=10)
# cats = Reference(sheet, min_col=1, min_row=1, max_row=10)
# chart = BarChart()
# chart.title = "Sales per Months"
# chart.x_axis.name = "Months"
# chart.y_axis.name = "Sales"

# chart.add_data(ref, titles_from_data=True)
# chart.set_categories(cats)
# sheet.add_chart(chart, "E5")
# wb.save("Chart3.xlsx")

#Now list apply this on line chart

# import openpyxl
# from openpyxl.chart import Reference,LineChart

# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet["A1"] = "Months"
# sheet["B1"] = "Sales"
# for i in range(2, 11):
#     sheet["A" + str(i)] = i
#     sheet["B" + str(i)] = i * 3

# ref = Reference(sheet, min_col=1,max_col=2, min_row=1, max_row=10)
# cats = Reference(sheet, min_col=1, min_row=1, max_row=10)
# chart = LineChart()
# chart.title = "Sales per Months"
# chart.x_axis.name = "Months"
# chart.y_axis.name = "Sales"

# chart.add_data(ref, titles_from_data=True)
# chart.set_categories(cats)
# sheet.add_chart(chart, "E5")
# wb.save("Chart4.xlsx")

#let's make scatter chart

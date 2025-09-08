# Merging and Unmerging Cells:
# to merge a number of cells with each other
# import openpyxl
# wb=openpyxl.Workbook()
# sheet=wb.active
# sheet['A1']='Twelve merged cells with each other.'
# sheet.merge_cells('A1:D3')
# sheet['D5']='Two merged cells'
# sheet.merge_cells('D5:E5')
# wb.save('merge.xlsx')


# import openpyxl

# wb = openpyxl.load_workbook("merge.xlsx")
# sheet = wb.active
# sheet.unmerge_cells("A1:D3")
# sheet.unmerge_cells('D5:E5')
# wb.save("unmerge1.xlsx")
#
# Freeze panes:
# is to freeze a few of the top row and the leftmost column onscreen
# forzen rows are visible to user as you scroll the spreadsheet
# if you set freeze_panes to B2 this mean that
# the row above it (B1) and the left column(A) will be frozen
# if freeze_panes(C2)->row C1 and left columns A,B are frozen
#
# import openpyxl
# wb=openpyxl.load_workbook('produceSales.xlsx')
# sheet=wb.active
# sheet['A1']='Wlcome to python'
# sheet.freeze_panes='C3'        #this mean row c2,c1 and A1,A2,B1,B2 this is the mean of the column of A and B
# wb.save('Freeze_panes.xlsx')


#
# Charts;
# openpyxl supports line,bar,scatter,pie chart
#
# to make a chart;
# create a reference object from a rectangular selection of cells
# create a series object by passing in it  the Reference object
# create a chart object
# Append the seies object in the chart object
# set the chart objects(drawing_left,drawing_width,drawing_height,drawing_top)
# Add the chartobject to the worksheet object.
# to make reference object
# openpyxl.charts.Reference()
# append to it three values:
# 1.worksheet object that contain on chart data
# 2.tuple of two values represent:top_left cell of rectangular selection of cells contain on two values:(rowvalue,columnvalue)
# 3.tuple of two integers represent:bottom_right cell of rectangular selection of cells :(rowvalue,columnvalue)

# import openpyxl
# from openpyxl.chart import Reference,Series,BarChart,LineChart,ScatterChart
# wb = openpyxl.Workbook()
# sheet = wb.active
# for i in range(1, 9):
#     sheet["A" + str(i)] = i

# refObj=Reference(sheet,min_row=1,min_col=1,max_row=8)
# srObj=Series(refObj,title_from_data=False)
# chrObj=BarChart()
# chrObj.append(srObj)

# chrObj.height=10  # this means the height of chart is 10 rows
# chrObj.width=30   # this means the width of chart is 10 rows
# # chrObj.series[0].name='First series'
# chrObj.title='First Series'
# chrObj.x_axis.title='X-axis'
# chrObj.y_axis.title='Y-axis'
# sheet.add_chart(chrObj,'C5')
# wb.save('Chart.xlsx')

# Making another Barchart ,LineChart  and Scatterchart on excel
import openpyxl
from openpyxl.chart import Reference,Series,BarChart,LineChart,ScatterChart
wb=openpyxl.Workbook()

sheet=wb.active

Data=[['Date','Sales','Profits'],
      ['Jenuary',1200,100],
      ['February',1300,150],
      ['March',1400,200],
      ['April',1500,250],
      ['may',1600,300],
      ['June',1700,350],
      ['July',1800,400]
      ]
for row in Data:
    sheet.append(row)       # this will append data into the excel
wb.save('Draw.xlsx')

refObjsales=Reference(sheet,min_row=1,max_row=7,min_col=2,max_col=2)
refObjProfits=Reference(sheet,max_col=3, min_row=1,max_row=7)
SerObj=Series(refObjsales,title_from_data=True)
Chart=BarChart()
Chart.append(SerObj)
sheet.add_chart(Chart,'C5')
sheet.setcategory
Chart.title='Sales'
Chart.width=10
Chart.height=10
Chart.x_axis.name='Sales'
Chart.y_axis.name='Profits'
wb.save('Draw2.xlsx')








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

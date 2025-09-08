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
# create a series object by passing in the Reference object
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

import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1, 9):
    sheet["A" + str(i)] = i
    # print(sheet["A"+str(i)].value)
refobj=openpyxl.charts.Reference(sheet,(8,1))


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

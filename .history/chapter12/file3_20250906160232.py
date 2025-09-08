# Creating and removing Sheets:
#
# import openpyxl

# wb = openpyxl.Workbook()

# sheet = wb.active
# print(sheet)
# sheet1 = wb.create_sheet(index=0)
# sheet2 = wb.create_sheet(index=2, title="Sheet2")
# sheet3 = wb.create_sheet(index=3, title="Sheet3")
# sheet4 = wb.create_sheet(index=4, title="sheet4")
# print(wb.sheetnames)
# wb.remove(wb["Sheet"])
# wb.remove(wb['Sheet1'])

# print(wb.sheetnames)

# wb.save('File1.xlsx')


# remove(worksheetobject)
# remove not take the sheetname just instead take worksheet object
#
# import openpyxl

# wb = openpyxl.load_workbook("File1.xlsx")
# print(wb.active)
# sh2 = wb["Sheet2"]
# for i in range(1, 100):
#     cells = sh2.cell(row=i, column=1)
#     cells.value = "Hello man!."
# print("Done.")
# print()
# wb.save("UpFile1.xlsx")
#
#
# Setting the font style of cell:

#
# to customize the font of text in excel: use font,style module from openpyxl

# import openpyxl
# from openpyxl.styles import Font

# wb = openpyxl.Workbook()
# sheet=wb.active
# italic24font=Font(size=25,italic=True)  # store inside italic24font (A font object with attributes (size and ittalic))
# sheet['A1'].font=italic24font
# sheet['A1']='Hello world!!!'
# wb.save('Font1.xlsx')
#
# write another word to the same excel file

# import openpyxl
# from openpyxl.styles import Font

# wb = openpyxl.load_workbook("Font1.xlsx")

# sheet = wb.active
# italic30Font = Font(size=30, italic=True)
# sheet["B1"].font = italic30Font
# sheet["B1"] = "Welcome to our Masjed"
# wb.save("Font2.xlsx")

# Font Object:
# Font()take : name (type of text (times new roman or default(Calibri))),size (always integer),bold(take True),italic(true)
#
# import openpyxl
# from openpyxl.styles import Font

# wb = openpyxl.Workbook()
# sheet = wb.active

# Name_bold = Font(name="Times New Roman", bold=True)
# sheet["A1"].font = Name_bold
# sheet["A1"] = "Times New Roman Bold"

# italic_size = Font(size=30, italic=True)
# sheet["B3"].font = italic_size
# sheet["B3"] = "Italic with size30"
# wb.save("Stayles.xlsx")


#
# the default size=11


#
# Formulas:
# it's begin with an equal statement
#
# import openpyxl
# from openpyxl.styles import Font

# wb = openpyxl.Workbook()
# sheet = wb.active
# add = 100
# for cel in range(1,9):
#     sheet.cell(row=cel,column=1).value=add
#     add+=100
# sheet['A9']='=SUM(A1:A8)'
# print('Done!')
# wb.save('Formula1.xlsx')

# we use '=SUM(A1:A8)'
# to sum all specified cells


#
# to read the function into the cell as a value or to read it's value
# pass to load_workbook(data_only=True)
import openpyxl

# wbformula = openpyxl.load_workbook("Formula1.xlsx")
# sheet = wbformula.active
# print(sheet["A9"].value)
# wbformula_data = openpyxl.load_workbook("Formula1.xlsx",data_only=True)
# sheet = wbformula_data.active
# print(sheet.cell(row=9,column=1).value)

#Adjusting Rows and Columns;
#using:row_dimension ,column_dimension
import openpyxl
wb=openpyxl.load_workbook()
sheet=wb.active
sheet['A1']='Hello to python'
sheet.row_dimensions[1:10].height=200       #Adjust all rows with this dimension
sheet.column_dimensions['B'].width=200      #Adjust all columns with this dimensions
sheet.column_dimensions['A'].width=200
wb.save('Dimension1.xlsx')
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

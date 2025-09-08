# Blank Row inserter:
# How it works:
# take two integers from the terminal : sys.argv N1 N2
# N1 -> the starting row
# N2 -> the number of blanck rows
# ---
# you will need to spreadsheet to read it
# then take two integers from user
# then write out the old spreadsheet into the new one
# then  by using for loop
# start at N1 row and put N2 rows blanck and write the rest of the old spread into the rest ones

# import openpyxl, sys

# try:
#     N = int(sys.argv[1])
#     M = int(sys.argv[2])
#     filename = sys.argv[3]
# except:
#     N = int(input("Enter the first number(starting to blank Row):"))
#     M = int(input("Enter the second number(Blanck Rows): "))
#     filename = input("Enter the name of the new file you want to save the old file to:")
# wb = openpyxl.load_workbook(filename)
# sheet = wb.active
# wb_new = openpyxl.Workbook()
# New_sheet = wb_new.active
# for row in range(1, N):
#     for col in range(1, sheet.max_column + 1):
#         New_sheet.cell(row=row, column=col).value = sheet.cell(
#             row=row, column=col
#         ).value
# for row in range(N, sheet.max_row + 1):
#     for col in range(1, sheet.max_column + 1):
#         New_sheet.cell(row=row + M, column=col).value = sheet.cell(
#             row=row, column=col
#         ).value

# wb_new.save(filename)
# print("Blink rows are added into the NewSheet.")

import openpyxl, sys

# --- Read arguments ---
try:
    N = int(sys.argv[1])  # starting row
    M = int(sys.argv[2])  # number of blank rows
    filename = sys.argv[3]
except:
    N = int(input('Enter the first number (starting row): '))
    M = int(input('Enter the second number (blank rows): '))
    filename = input('Enter the filename: ')

# --- Open original workbook ---
wb = openpyxl.load_workbook(filename)
sheet = wb.active

# --- Create new workbook ---
new_wb = openpyxl.Workbook()
new_sheet = new_wb.active

# --- Copy rows before N ---
for row in range(1, N):
    for col in range(1, sheet.max_column + 1):
        new_sheet.cell(row=row, column=col).value = sheet.cell(row=row, column=col).value

# --- Copy rows from N to end, shifted by M ---
for row in range(N, sheet.max_row + 1):
    for col in range(1, sheet.max_column + 1):
        new_sheet.cell(row=row + M, column=col).value = sheet.cell(row=row, column=col).value

# --- Save result ---
new_wb.save('Project4.xlsx')

#
#
#
#
#
#
#
#

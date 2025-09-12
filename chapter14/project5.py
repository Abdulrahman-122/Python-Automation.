# Excel to CSv converter:
# convert any excel sheet in your os.listdir
# into a CSVs file
# where: each sheet in the excel sheet should be into
# new Csvs file
# note: name each Csvfile as : excelname_sheetname.csv
# what should you use in this program:
# os.listdir  to get all excel sheet
# use:
import openpyxl, csv

# use many for loops and
# open()method
import os, openpyxl

files = [file for file in os.listdir()]
excelfiles = [file for file in files if file.endswith(".xlsx")]
for file in excelfiles:
    wb = openpyxl.load_workbook(file)
    for sheet in wb.sheetnames:
        sh = wb[sheet]
        filewithoutextention = file[:-5]
        sheetname = sheet
        Csv_newfile = filewithoutextention + "_" + sheetname + ".csv"
        fileobj = open(Csv_newfile, "w")
        writer = csv.writer(fileobj)
        for i in range(1, sh.max_row + 1):
            rowData = []
            for j in range(1, sh.max_column + 1):
                # hold each row in excel sheet
                whole_row = sh.cell(row=i, column=j).value
                rowData.append(whole_row)
            writer.writerow(rowData)
        print(f"The sheet:{sheetname} in file:{file} -> {Csv_newfile} Done.")
        fileobj.close()

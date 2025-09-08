# write a spreadsheet into a textfile:

import openpyxl

wb = openpyxl.load_workbook("produceSales.xlsx",data_only=True)
sheet = wb.active
lines1 = []
#see the excel How many columns in it and make the same with new lists I make here 4 as the produceSales.xlsx contain on 4 columns 
columna = []
columnb = []
columnc = []
columnd=[]
for row in range(1, sheet.max_row):
    columna.append(sheet["A" + str(row)].value)
    columnb.append(sheet["B" + str(row)].value)
    columnc.append(sheet["C" + str(row)].value)
    columnd.append(sheet['D'+str(row)].value)
#check here by print the lists of columns to see are ther
with open("File7.txt", "w") as file1:

    
    for item1, item2, item3,item4 in zip(columna, columnb, columnc,columnd):
        try:
            file1.write(f"{item1}  {item2}  {item3:.2f} {item4} \n")  # this apply for any number not a string in it self  
        except:
            file1.write(item1 + " " + str(item2) + " " + str(item3)  +" "+ str(item4) +'\n')     # this apply for any string not a number in it self


#note : at row 1 item 2, 3 ,4 is not a number they are a strings so we make this try except code to solve this issue

print("Done.")
 
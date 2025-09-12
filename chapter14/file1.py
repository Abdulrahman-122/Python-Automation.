# Working with Csv Files and Json Data:
# Csv,Json is a plain text can be appear int the text editior
# instead of pdf or docx that was binary data
# so : python we use modules Csv,json to work with these files
#
# Csv -> it's called: comma-separated values
# it's a simplified spreadsheets stored as plaintext files
# it's easy to parse Csv files by python
#
# Json -> called: Jay-sawn or Jason
# it's a format that stores information as javascript source code in a plaintext files.
# it's a javascript object notation
# it's useful now as it uses in many Applications


# The Csv Module:
# each line in it like a row in a spreadsheet that hold a plaintext
#
# Csv files:
# Don't have type for it's values -> everything is a string
# Don't have setting for fontsize or color
# Don't have multiple worksheets
# can't specify cell widths and heights
# can't have merged cells
# can't have images or charts embedded in them.
# it's advantages:
# simplicity
# it's a straightforward way to represent spreadsheet data
# textfile of comma separated values


# Read Csv:
import csv

file = open("example.csv")
reader = csv.reader(file)
Data = list(reader)
# print(Data)
#
# you don't need to import csv as it come with python
# to read csvfile
# open it with open()
# pass the fileobj to csv.reader()->return a reader object to use
# note: you can't pass a the filename to csv.reader()
# to access the values in reader
# pass it to the list()-> return a list of lists
#
# to access data : Data[row][col]
for list in Data:
    if list == []:
        continue
    print(list)
    # for i in range(0,3):
    #   print(list[i])

# Reading Data from Reader Objects in a for loop:
import csv

exampleFile = open("example.csv")
reader = csv.reader(exampleFile)
Newfile=open('example_updated.csv','w',newline='')
writer=csv.writer(Newfile)
for row in reader:
    print('Row#'+str(reader.line_num)+str(row))
    writer.writerow(row)
Newfile.close()
    # print(reader.line_num)
    # print(row)



# here :
# using reader object in a for loop can show all objects
# reader.line_num -> return the number of row in the reader list


# Write objects:
# enable you write to csv file
# you should create a writer object
# csv.writer()


# import csv
# file=open('output.csv','w',newline='')
# writer=csv.writer(file)
# writer.writerow(['spam','eggs','bacon','ham'])
# writer.writerow(['Hello,world','eggs','bacon','ham'])
# writer.writerow([1,2,3.141592,4])
# file.close()


# notice that the writer object escapes the comma in Hello,world with making double quotes
import csv

# file = open("Newfile.csv", "w", newline="")
# writer = csv.writer(file)
# writer.writerow(["Welcome", "Hello", "Yeah", "Hi"])
# writer.writerow(["Spam", "Bacon", "Eggs", "ham"])
# writer.writerow([1, 2, 3, 4, 56, 6, 7, 8.122233])
# writer.writerow(["end", "end", "end", "end", "end"])
# file.close()
# you put newline='' :make the rows under each other no space between rows
# we use csv.writer() return a writer object
# writerow() used to write a a writer object that takes alist
# each item in the cell is put inside one cell in the csv
# return value from writerow -> is the number of characters  writter for the row in csv including newline characters

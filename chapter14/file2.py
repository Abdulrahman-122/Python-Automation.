# The delimiter and lineterminator keyword  Arguments:
# you want the cells with tab character instead of comma
# you want the rows to be doubled-spaced
# import csv
# file=open('file.tsv','w',newline='')
# writer=csv.writer(file,delimiter='\t',lineterminator='\n\n')
# writer.writerow(['apples','oranges','grapes'])
# writer.writerow(['eggs','bacon','ham'])
# writer.writerow(['spam','spam','spam','spam','spam','spam'])
# file.close()

# the delimiter:is the characters that appear between cells on row
# default delimiter=comma
# lineterminator -> the character that come at the end of a row
# lineterminator by default is a newline
# all of these you put in csv.writer(delimiter='',lineterminator='')
# if you find any problem as no delimiter is applied on excel then use .tsv
# which means the tab will applied but when you open the file in notabad format.

import csv

file = open("example.csv", "r")
reader = csv.reader(file)
for item in reader:
    if item == []:
        continue
    # print(item[1])
    # print(item[2])
    # print(item[0])

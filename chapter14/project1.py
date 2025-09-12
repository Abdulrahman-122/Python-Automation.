# Removing the Header from Csv files:
# open every csvfile in your working directory:
# read the contents of the Csv file
# rewrite the content without the first row to a file of the same name
# this will save the csv file with the new.
#
# the program must do the following;
# find all csv files in the current working directory
# Read the full contents of each file
# write out the contents+skip the firest line to a new csv file
#
# so the program will need to do :
# loop over a list of files from os.listdir()
# skipp the non-csv files
# create csv reader to read the contents of file
# use line_num attrib to figure out which line to skip
# create a csv writer object and writer out the read_in data to the new file.
import csv, os

csvfiles = []
for file in os.listdir():
    if file.endswith(".csv"):
        csvfiles.append(file)
# print(csvfiles)

for index, file in enumerate(csvfiles):
    file_object = open(file)
    reader = csv.reader(file_object)
    fullfilename = file[:-4] + "_updated.csv"
    Newfile_object = open(fullfilename, "w", newline="")
    writer = csv.writer(Newfile_object)
    for row in reader:
        if reader.line_num == 1:
            # writer.writerow([])  # this line will shift the first row in excel down to the second row (but I didn't remove)
            continue  # while this line will remove the file by the all.
        if reader.line_num == 2:
            writer.writerow(
                []
            )  # shift down the second item that go up to the first row after remove the first row

        if row == []:
            continue

        else:
            writer.writerow(row)
    Newfile_object.close()
    print(f"file#{index} :{file} is updated(check it).")
print("Done")


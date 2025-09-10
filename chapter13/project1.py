# Combining select pages from many PDFs:
# if you have a dozens of pdf files and you want to
# combine some pages from each file
#
# what's the program do?
# find all Pdf files in the current working directory
# sort the filenames so the pdfs are added in order
# write each page execluding the first page to the output page
# implementation of program:
# call os.listdir() to find any files in the working directory + remove any non-pdf files
# call sort() to alphabetize the filenames
# creat PdfWriter ( ) to create the ouput pdf file
# loop over each pdf file -> by creating a pdf reader file for them
# loop over each page in each pdf file except the first page
# add the pages to the output file
import os
from pypdf import PdfReader, PdfWriter

files = [f for f in os.listdir() if f.endswith(".pdf")]

writer = PdfWriter()

files.sort()
for file in files:
    with open(file, "rb") as openedfile:
        reader = PdfReader(openedfile)
        for page in range(1, len(reader.pages)):
            writer.add_page(reader.pages[page])
with open("Combining.pdf", "wb") as outfile:
    writer.write(outfile)
print("Done Combining.")
# run this program at Test_the_Projects as there are encrypted files that python can't open it with decryption and I didn't add it here.
# you can add it decryption
# notes:
# if you have more than pdf and want to sort them alphabatic either small or capital char
# [b.pdf,C.pdf,a.pdf]-> use files.sort(key=str.lower) -> [a.pdf,b.pdf,C.pdf](called : case-insensetive)
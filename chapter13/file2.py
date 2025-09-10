# now the problem is : you can't edit the pdf you just copy the content of old file and add it to new one you want
#
# now : you can
# create many pdfReader object  for more than one pdf file
# then create pdfWriter object                    -> this make a value that represent just pdf document in python
# copy pages from pdfReader to the pdfWriter object
# use the pdfWriter the write the output pdf file  by using write() and open(newfile.pdf,'wb')
#
# wb -> write binary mode
#
# by using this -> you can cut unwanted pages,reordered pages , combine multiple pages
#
# Let's combine two pdf files that is already hold on information into a newone that we will create it

# from pypdf import PdfWriter, PdfReader

# file1obj = open("meetingminutes.pdf", "rb")  # add rb -> read binary mode
# file2obj = open("meetingminutes2.pdf", "rb")

# readfileobj1 = PdfReader(file1obj)
# readfileobj2 = PdfReader(file2obj)
# writer = PdfWriter()

# for page in readfileobj1.pages:
#     writer.add_page(page)
# for page in readfileobj2.pages:
#     writer.add_page(page)
# with open("compine.pdf", "wb") as newfile:  # add wb as write binary
#     writer.write(newfile)
# print("The operation is successed.")


# Rotating pages;
# you can use rotate(value) -> value 90(90 degrees) or -90 or 180 or 270
# add the rotation on the page of the current  file and then pass this change to another file
# from pypdf import PdfReader, PdfWriter

# file1obj = open("meetingminutes.pdf", "rb")
# reader = PdfReader(file1obj)

# page = reader.pages[0]
# page.rotate(180)
# writer = PdfWriter()  # make pdf file object
# writer.add_page(page)
# with open("rotate.pdf", "wb") as rot:
#     writer.write(rot)
# print("Rotation made successfully")


#Overlaying pages:
#pypdf can overlay content of one page over the other
#and this help us to add a logo ,timestamp,watermark
#you can add watermark to multiple pages
# from pypdf import PdfReader,PdfWriter
# file1obj=open('meetingminutes.pdf','rb')
# water1obj=open('watermark.pdf','rb')

# read1=PdfReader(file1obj)
# read2=PdfReader(water1obj)

# writer=PdfWriter()

# pagezerofile1=read1.pages[0]
# watermarkpage=read2.pages[0]

# pagezerofile1.merge_page(watermarkpage)   #merge watermark on the first page of file1
# writer.add_page(pagezerofile1)             #should it this page to the writerobj

# for page_num in range(1,len(read1.pages)): #note we start from page 1 not 0 as it's actually merged if you write 0 this mean all above work will be overwritten
#     writer.add_page(read1.pages[page_num])

# with open('merged.pdf','wb')as merge:
#     writer.write(merge)
# print('Done.')



#to add watermark to all pages of the file

from pypdf import PdfReader,PdfWriter
file1obj=open('meetingminutes.pdf','rb')
water1obj=open('watermark.pdf','rb')

read1=PdfReader(file1obj)
read2=PdfReader(water1obj)

writer=PdfWriter()

watermarkpage=read2.pages[0]   # bring first page of watermark

for page_num in range(0,len(read1.pages)):  
    pagefile=read1.pages[page_num]   # bring all pages of file1
    pagefile.merge_page(watermarkpage)   # merge with each page the watermark
    writer.add_page(pagefile)         # then add this merged page to the writer pdf

with open('merged1.pdf','wb')as merge:
    writer.write(merge)
print('Done.')
#to make new encryption pdf by adding to it the old data
from pypdf import PdfReader,PdfWriter
fileobj=open('merged.pdf','rb')
read=PdfReader(file1obj)
writer=PdfWriter()
writer.encrypt(user_password='1234',owner_password='4321')
for page in read.pages:
    writer.add_page(page)
with open('encrypt.pdf','wb') as encrypt:
    writer.write(encrypt)
encrypt.close()
print('Done.')











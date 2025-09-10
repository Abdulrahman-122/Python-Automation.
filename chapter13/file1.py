# pdf, word files are binary files
# so you can't work with it by using simple (open()) to access these files
# we will learn : PyPdf2,python_Docx
#
# Pdf -> portable document files uses     .pdf ext
# I will use many modules
# run it by : pip install pypdf or fitz.... in the terminal
# import pypdf
# import pdfplumber
# import fitz
# from reportlab.pdfgen import canvas

# Extracting Data from a Pdf using : PyPDF2
# import pypdf

# with open("meetingminutes.pdf", "rb") as file1:
#     reader = pypdf.PdfReader(file1)
#     print(len(reader.pages))

#     page = reader.pages[0]
#     text = page.extract_text()
#     print(text)

#     page = reader.pages[5]
#     text = page.extract_text()
#     print(text)


# we use
# importing pypdf
# pypdf.pdfReader(file) -> to make pdf fileobj
# .pages[numofpage] -> to get the page obj
# .extract_text -> to extract text from file.
#
# or using the fitz ->PyMuPDF        but you will see there are some missing
# import fitz
# doc=fitz.open('meetingminutes.pdf')
# for page in range(len(doc)):
#     textobj=doc[page]
#     page_text=textobj.get_text()
#     print(f'Pagenumber:{page+1}')
#     print(page_text)


# Decrypting Pdfs:
# which means that you can't open any pdf file under get the password to open it
# let's make new pdf and then encrypt it with a new password

# from pypdf  import PdfWriter

# writer=PdfWriter()

# writer.add_blank_page(width=300,height=300)
# writer.encrypt(user_password='user123',owner_password='owner123')
# with open('file1.pdf','wb')as f:
#     writer.write(f )
# print('Encrypted Pdf successfully is created.')


# user_password -> to open the pdf / owner_password -> to make changing to the password.

# lets try to open an encrypted pdf file using : pypdf module

# import pypdf

# reader = pypdf.PdfReader("encrypted.pdf")
# print(reader.is_encrypted)

# reader.decrypt(
#     "rosebud"
# )  # without this line the file didn't open to show to you it's contents.
# page = reader.pages[0]
# print(page.extract_text())

# Let's do another example:make new file and then encrypt it then decrypt it and open it's contents
from pypdf import PdfReader, PdfWriter

Reader = PdfReader("meetingminutes.pdf")
writer = PdfWriter()

# copy all the contents from original file to the new one
for page in Reader.pages:
    writer.add_page(page)
writer.encrypt(user_password="123", owner_password="321")
# Let's make newfile

with open("Newmeetingminutes.pdf", "wb") as f:
    writer.write(f)
print("File is encrypted and made successfully")

# let's check the newfile data
reader = PdfReader("Newmeetingminutes.pdf")
print(reader.is_encrypted)
# Let's decrypt it with user_password
reader.decrypt("123")
page = reader.pages[0]
print(page.extract_text())
#Let's save the data of this page to another file
writer2=PdfWriter()

writer2.add_page(page)
with open('page zero .pdf','wb') as info:
    writer2.write(info)







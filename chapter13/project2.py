# PDF Paranoia:
# use os.walk()
# write a script
# go through every pdf in folder, and subfolder
# encrypt all these files using a password provided on the command line.
# save each encrypt pdf with an _encrypted.pdf
# then Deleting the original file     (I will do it's code but I will ignore it as I need the original files you can do it if you want)
# then make a program :
# to read and decrypt the file to ensure it's encrypted correctly
# then write a program to find all encrypted PDFs in a folder
# and creates  a decrypted copy of the pdf using a password
# if the password is incorrect -> print a message to the user and go to the next pdf
import pypdf, os, pypdf, sys
from pypdf import PdfReader, PdfWriter

for item in os.walk("D:\python_content\python_Automation_part2\chapter13"):
    files = item[-1]
# print(files)
pdffile = []
for file in files:
    if file.endswith(".pdf"):
        pdffile.append(file)
# print(pdffile)
Encrypted_files = []
try:
    writer = PdfWriter()
    for file in pdffile:
        fileobj = open(file, "rb")

        reader = PdfReader(file)

        if reader.is_encrypted:
            continue

        for page in reader.pages:

            writer.add_page(page)

        print(f"Now will encrypt this file{file} with this password:{sys.argv[1]}.")

        writer.encrypt(
            user_password=sys.argv[1], owner_password="1234"
        )  # the last time I entered password:12345 in command line

        print("  file now add to  _encrypted.pdf and will be saved")

        prefixfilename = file[:-4]

        Newfile = prefixfilename + "_encrypted.pdf"
        # os.remove(file)                   # if you want to remove file
        with open(Newfile, "wb") as newfile:

            writer.write(newfile)

            newfile.close()

        print(f"finsh saving this file {Newfile}: let's move on the Next one....")
        Encrypted_files.append(Newfile)

        print("Now: Let's open the encrypted files ")
        print("Decrypt the files one by one  with each Decrypt then we should read it")
        print("Done.")

except:
    print("Maybe you're not enter the password in the command when you run the program")
    print("Maybe you encrypt this file once and you try to do this again .")
    for file in pdffile:
        if file.endswith("_encrypted.pdf"):
            Encrypted_files.append(file)

writer = PdfWriter()
count = 0
try:
    for file in Encrypted_files:
        count += 1
        reader = PdfReader(file)
        print(f"Enter the password to open {file} and read it.")
        pas = input(">")
        reader.decrypt(pas)

        for page in reader.pages:
            writer.add_page(page)
        print("File added to the writer.")
        #    print(page.extract_text())
        # print(f'Finish content of file: {file,count}.')

        print("#" * 50)
    wholefile = input("write name for newfile to merge in it all files(.pdf)>>  ")
    with open(wholefile, "wb") as newfile:
        writer.write(newfile)
    print("Done.")
except:
    print(
        "You enter a false password (remember the last pass you encrypt files with (remember either the user or owner pass you attatch files with))"
    )

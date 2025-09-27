# Let's make a complete program for sending email
# import smtplib

# smtpobj=smtplib.SMTP('smtp.gmail.com',587)
# smtpobj.ehlo()
# encryption=smtpobj.starttls()
# print('Enter App pasword.')
# Secret_pass=input('>')
# login=smtpobj.login('abdulrahman11510.qasim@gmail.com',Secret_pass)
# subject='Welcom Abdulrahman:'
# message='This is your python script send greeting to you \n Ready for Linux World.'
# body=f'{subject}\n\n {message}'
# send_mail=smtpobj.sendmail('abdulrahman11510.qasim@gmail.com','abdulrahman11510.qasim@gmail.com',body)
# smtpobj.quit()
# print('Email send Successfully....')

# let's make a complete program to dray this email and then complete it okay:
#
import imapclient, pyzmail, imaplib

imapobj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
print("Enter App pasword.")
Secret_pass = input(">")
ligin = imapobj.login("abdulrahman11510.qasim@gmail.com", Secret_pass)
folders = imapobj.list_folders()
folder = imapobj.select_folder("INBOX", readonly=False)
allemails = imapobj.search("All")
github = imapobj.gmail_search("github")
print(github)
fetch = imapobj.fetch(github[1], ["BODY[]"])
# print(fetch)
firstemail = github[1]
pyzobj = pyzmail.PyzMessage.factory(fetch[firstemail][b"BODY[]"])
print(pyzobj.get_subject())
print(pyzobj.get_addresses("to"))
print(pyzobj.get_addresses("from"))
print(pyzobj.get_addresses("cc"))
if pyzobj.text_part != None:
    print("Yeah it contain on text part(let's print it)")
    print(pyzobj.text_part.get_payload().decode(pyzobj.text_part.charset))
if pyzobj.html_part != None:
    print("Yeah it contain on html part(let's I will not print it)")
    pyzobj.html_part.get_payload().decode(pyzobj.html_part.charset)
imapobj.delete_messages(firstemail)
imapobj.expunge()
print(f"this mail deleted {firstemail} successfully. ")
imapobj.logout()
print("Done")

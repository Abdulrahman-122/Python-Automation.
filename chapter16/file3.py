# Getting Email Addresses from a Raw Message:
# as the returned value from fetch not easy to understand by people
# so we use pyzmail to return clair message from email
# that contain on from : to: body of message
# first:
# install pyzmail36
# then
# import pyzmail36 as pyzmail
# make pyzmail object by :pyzobj= pyzmail.pyzMessage.factory(rawMessages[40041]['BODY[]'])
# now use this object's function now
# get_subject() -> return the subject of email in a string format easily
# get_addresses(pass)    pass='from' or 'to' or 'cc' or 'bcc'
# and this return a list of tuples which each tuble contain on : firstitem(name person that related to email) second:(his email) if the no addresses get_addresses return an empty list
#
# 
# # Getting a body from the message:
# email can be send as plain text or Html or both
# plaintext email contain only on a text
# while Html email contain on fonts , colors, fonts,auther features
# and this make the email with html like a small web page
# 
# if email is an plain text -> pyzMessage will set it's html_part attributes to None
# if email is an Html  -> pyzMessage will set it's text_part to None
# where text_part() and html_part() have a get_payload() that returns the email's body as a value of bytes datatype
# then put this return by get_payload() as argument to decode() 
# this return we put into get_payload.decode(text_part.charset or html_part.charset) then this will return the string of the email's body+html of body of each part
# 
#Deleting emails:
#to delete an email
#pass the list of uids you want to delete into (imapobj.delete_messages(uids))
#no call imap.expunge() will delete the uid you specify with delete_messages
# note:(When, no messages are specified, remove all messages from the currently selected folder that have the \Deleted flag set.)
# after you finishing retrieve email or delete it
# you need to disconnect from imap server()
# use: imapobj.logout() 
# 

import imapclient, pprint
import pyzmail


imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
print("Enter your Secret password????")
Apppassword = input(">")
login = imap_obj.login("abdulrahman11510.qasim@gmail.com", Apppassword)
allfolder = imap_obj.list_folders()
# print(allfolder)
folder1 = imap_obj.select_folder("[Gmail]/Spam", readonly=False)
# print(folder1)
UIds = imap_obj.search("ALL")
# print(UIds)
fetch1 = imap_obj.fetch(UIds[-4:], ["BODY[]"])
fetch1_info = imap_obj.fetch(UIds[-4:], ["ENVELOPE"])

# pprint.pprint(fetch1)
# pprint.pprint(fetch1_info)
anotherfolder = imap_obj.select_folder("INBOX", readonly=False)
UIds = imap_obj.search("ALL")
# print(UIds)
fetch = imap_obj.fetch(UIds[-2], ["BODY[]"])


beforelast=UIds[-2]    # the second email from right at UIDs  list 

beforelast_message=pyzmail.PyzMessage.factory(fetch[beforelast][b'BODY[]'])


print(beforelast_message.get_subject())
print(beforelast_message.get_addresses('to'))
print(beforelast_message.get_addresses('from'))
print(beforelast_message.get_addresses('cc'))
print(beforelast_message.get_addresses('bcc'))
print(beforelast_message)
#make sure the type of email is it writtin in html or just a plaintext
#let's bring the plaintext part and html_part

if beforelast_message.text_part!=None:
    print('Yeah this email is writtin in plain text')
    print('This is the body tha\'s written in plain text')
    print(beforelast_message.text_part.get_payload().decode(beforelast_message.text_part.charset))
    
if beforelast_message.html_part!=None:
    print('Yeah, This email is writtin in Html code.')
    print('This is the body tha\'s written in Html text')
    print(beforelast_message.html_part.get_payload().decode(beforelast_message.html_part.charset))

del_UId=UIds[1400]
del_mess=imap_obj.delete_messages(del_UId)
expung=imap_obj.expunge()
# print(del_mess)
# print(expung)
imap_obj.logout()

#Don't forget to but b before "BODY[]" to indicate that it's a bytes as eamail contain on binary data , encoded ..... so it's stored as bytes type not string
# while in fetch you don't need to put b before ['BODY[]'] as it's actually stored it init like: fetch = { 1234(UID number): { b'BODY[]': b"raw email data" } }
# 
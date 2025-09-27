# lets send another email to the same first email
# import smtplib

# smtpobj=smtplib.SMTP('smtp.gmail.com',587)
# greeting=smtpobj.ehlo()
# encryption=smtpobj.starttls()
# print('Enter App Password???')
# my_secret_pass=input('>')
# loggingwithserver=smtpobj.login('abdulrahman11510.qasim@gmail.com',my_secret_pass)
# info="subject:Dear Aaisha\n\n This is your brother Abdulrahman Qasim\nI've some good news for you \n If you study hard you will get extraordinary results." \
# "Sincerly: Abdulrahman Qasim"

# message=smtpobj.sendmail('abdulrahman11510.qasim@gmail.com','jklmno1236p@gmail.com',info)
# smtpobj.quit()
# print('Message is sending ')


# here is send the message to my self it's piece of cake
# smtpobj=smtplib.SMTP('smtp.gmail.com',587)
# greeting=smtpobj.ehlo()
# encryption=smtpobj.starttls()
# print('Enter App Password???')
# my_secret_pass=input('>')
# loggingwithserver=smtpobj.login('abdulrahman11510.qasim@gmail.com',my_secret_pass)
# info="subject:Dear Aaisha\n\n This is your brother Abdulrahman Qasim\nI've some good news for you \n If you study hard you will get extraordinary results." \
# "Sincerly: Abdulrahman Qasim"

# message=smtpobj.sendmail('abdulrahman11510.qasim@gmail.com','abdulrahman11510.qasim@gmail.com',info)
# smtpobj.quit()
# print('Message is sending ')


# IMAP:(internet message access protocol)
# is a protocol for sending email
# it's communicate with your email provider to retrieve email sent to your email address
# you can use imaplip but the easier is ImapClient
# and pyzmail36 to parse email messages(text) for you
# steps to retrieve  and extract message
#
# 1.connecting to imap server:to get imapclient object
# you need imap server to reveive email
# you need your email provider's domain name
# for Gmail: imap.gmail.com
# put them into imapclient.IMAPClient('domainname',ssl=true)
# ssl -> most email provider's require it as encryption so put it as True
# 2.logging into the Imap server
# imapobj.login('youremail','app password')
# remember to write code from input() not in your code
# you should use application specific password to agree with gmail server
# go to application specific password to know how to use it on google
# 3.Searching for Email:
# to retrieve email you want -> select a folder you want to search through
# then call IMAPClient object's search()
# the output of this operation : list of tuples   each tuple contain on one tuple
# say:(('\\hasnoChildren),'/','INBOx') -> this mean
# the first item called: folder's flag (tuble inside tuble) it's the properties of folder (like : has nochildren (means:no subfolders inside this folder)or has childrens (means has a supfolders inside it),'//nonselect'(means you can't select from this folder))
#
# the second item called: the delimeter used in the name string used to separate parent from subfolders
# the third item ; full name of folder (parent folder)
# 4.select folder you want to search for using: select_folder(foldername,readonly=True)
# Note that we use:readonly to gurntee that we don't remove any messages from that folder unless you want to change
# 5.search for eamail you want;
# using imapobject.search()to search for
# a.if you want to see all messages in the folder you choice-.
# use imapobj.search('All') -> this means that you will return all the messages in the folder
# but this will exceeds the maximum limit of message and python will return an imaplib.error so to solve it
# as the default size=10000s bytes
# if you want more
# import imaplib
# imaplib._MaxLINE=10,000,000
# b.if you want to return a message before a specific date or on it or since it(at that date or after it)
# 'BEFORE 05-Jul-2015' or 'on '05-Jul-2015'' 'since '05-Jul-2015''
# c.if you want to return a messages where the string you want to search for in found in
# 'SUBJEECT "string you want"' or "BODY"string you want "" or "Text "String you want""   0> we put string inside a double quotes if it contain on spaces
# d.if you want to return a message by using email addresses
# From emailaddress
# TO   emailadress
# CC   email addresses   any email you copy messages to it so the email TO part will see him(carbon copy)
# BCC  secret email address any email you send message to him but not anyone in TO or CC part can see him (blind carbon copy)
# and thers's more return to it (page 370)
# 6.Fetching and making email as read
# to get the actual email content : use imapobj.fetch(UIDs,['BODY[]]) from  the list of UIDs
# ['BODY[]'] which tells UIds to download all the body content of the UIds in your list
# also use pprint to show the email in nice way



import imapclient, pprint

Imapclient_obj = imapclient.IMAPClient(
    "imap.gmail.com", ssl=True
)  # return an IMAPclient object
print("Enter the App password???")
app_password = input(">")
login = Imapclient_obj.login(
    "abdulrahman11510.qasim@gmail.com", app_password
)  # if it return authentication success this mean you are connect with your google
# print(login)
folders = Imapclient_obj.list_folders()
# print(folders)
# pprint.pprint(folders)      # for prity print to easy read hardlines
connect_Inbox = Imapclient_obj.select_folder("INBOX", readonly=True)
# print(connect_Inbox)
All_UIDs1 = Imapclient_obj.search(
    "ALL"
)  # return a list of UIDS(unique identifier) where each message has a number from those
Since_UIDS2 = Imapclient_obj.search("SINCE 05-Jul-2025")
# print(Since_UIDS2)
BODY_UIDS3 = Imapclient_obj.search('BODY "Hello Abdulrahman"')
# print(BODY_UIDS3)
search_engine = Imapclient_obj.gmail_search(
    "Sleep success: My journey to better rest"
)  # you can search on any email using gmail.search instead of the last methods we made to extract specific email
# print(search_engine)
# fetch1 = Imapclient_obj.fetch(All_UIDs1, ["BODY[]"])
# fetch2 = Imapclient_obj.fetch(search_engine, ["BODY[]"])
# fetch = Imapclient_obj.fetch(search_engine[1], ['ENVELOPE'])
fetch = Imapclient_obj.fetch(search_engine[1], ['BODY[]'])

pprint.pprint(fetch)

# print(fetch2)

# the output of this program :
# is a dictionary with key=Uid number and it's value is a nested dictionary
# where this nested dictionary contain on two keys ;'BODY[]'(contain on the body of email),SEQ(sequance number) it's similar to UIds in the role
# the message in 'BODY[]' is in a format called : RFC 822 designed for IMap server
# as you put in search_folder -> readonly=false this mean the message is for read but in fetch it will not marked as read so to fix this
# change it's value to False
# after you doing this ; you can call any folder with from the search in the imapobj not just it
#
#
# use ['ENVLOPE'] to show the info about the sender and from where.....

# Sending Email and Text Messages:
# you can use python to write a related emails
#
# as if you have a spreadsheet and contain on employees
# each employee has age and name
# so you can send for each one specific eamail fast rather than copy paste
#
# you can also send some sms while you are out of home
# and your phone will tell you about it
#
# SMTP:(simple mail transfer prtocol)
# it's like Http
# used to send web pages acrosss the internet
# it's dictates how email messages should be formatted ,encrypted , relayed between mail servers
# + dictates all technical  info that your computer needs to send messages

# you don't need to know these technical info as python smtplib module smplifies these into few functions
# How to send Email:
# 1.connect to SMtp server
# the domain name of SMTP server is = the name of your email provider domain name with .smtp in front of it
# if my email driver is : gmail.com=> smtp.gmail.com(domain name)
#
# 2. create an smtp object:by using: smptlip.smtp('domainname',port)
# port=> is an integer always be 587  which is used by command encryption standerd TLs
# 3.now you make SMTP object which is the connection to the SMTP server
# also this object has a methods to send email
# 4.make greeting for the server (or connect with server) using ehlo() method
# 5. if you use port 587 -> this mean you use TTl encryption to enable it with your server use starttls()
# if you use port =465 you enabled with encryption no need for doing this step
# 6.logging into the smtp server
# after making encryption
# you use your email address(username) and email password(your password)
# smtpobj.login('email','password')
#password you make on Google for this program as modern Google doesn't use it's password to connect with this program
#instead google provide feature called: APP password to connect with old apps and services that doesn't support modern standards to sign in
#7.sending an email :
# using : smtpobj.sendmail('my emial','recipient email','bodyof email')
# recipient -> may be someone or many if you send to someone put email of him into a string
# if many put emails of them into alist
# body of email => start with 'subject:\n
# any message you want
# 
# '
# for anyone you send to it and failed the sending -> then it will return a dictionary with key value in it
# if all emails that you send  to  is agree and took the message -> python will return an empty dictionary
# 
# 
# 8.quit connection with smtp server  if the output of it is 221 this mean the session is ending



# import smtplib

# smtpobj = smtplib.SMTP(
#     "smtp.gmail.com", 587
# )  # we make a smtp object and we now connecting to smtp server
# print(type(smtpobj))  # this tells you that there's SMtP object stored in smtplip

# greet_server = smtpobj.ehlo()
# # print(greet_server)
# encryption = smtpobj.starttls()
# # print(encryption)
# print('!!!Enter App password!!!')
# My_secret_password=input('>')
# loggin = smtpobj.login("abdulrahman11510.qasim@gmail.com", My_secret_password)
# # print(loggin)
# message=smtpobj.sendmail(
#     'abdulrahman11510.qasim@gmail.com','jklmno1236p@gmail.com','Supject:\n Welcome Aaisha\nThis is your bro Abdulrahman\nThis is a test just don\'t be afraid.'
# )
# print(message)
# smtpobj.quit()

# not without smtp object you can't use any method that makes you  send email
# if Smtplib.smtp() is  not successful this mean port is false(which yout smtp main server not support TLS on this Port )
# in this case you will make smtp object using(smtp_ssL,port=465)
# smtpobj=smtplib.smtp_ssL('smtp.gmail.com',465)
# if you not connect to internet -> python return error=socket.gaierror or [Errno 11004]
#
# TTL , ssL isn't important to know
# you need to know
# which encryption standered  your Smtp server uses in order to connect it
# after you connect with server or saying to it hello server using ehlo ()
# if the return value contain on 250 this mean your connection is correctly and your smtp object is correct
# 220 out of  ttle encryption tells your server is ready
#235 as output from logging to gmail server make sure that your authentication was successful
#if not python will raise a smtplip.smtp authentication error for incorrect passwords
#
#don't put this password in the sourcecode as may any hacker or theif take it and get access to your gmail
#instead using input ()and type in it the App password(my secret password)
#
#
#
#
#
#
#
#



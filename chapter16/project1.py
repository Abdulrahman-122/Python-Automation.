# Sending Member Dues Reminder Emails:
# if you a voulnteered to Volunteerism club
# you want to send a Dues reminder emails for whom someones who didn't pay for this month
#
# At a high level what's your code should do:
# Read data from an excel spreedsheet
# find all members who haven't paid for the latest month
# find their email addresses and send a them personalized reminders
# so your code will do the following:
# open and read cells of spreadsheet with openpyxl
# create a dictionary of memebers who are behind their dues
# login in smtp server by calling: smtplib.smtp()-> ehlo-> starttls()-> login()
# for each one that behind his due -> send a personalized reminder by calling sendmain()

# I make this step in order to put correct email to send to to see is this program will work or not

# import openpyxl
# wb=openpyxl.load_workbook('duesRecords.xlsx')
# acti=wb.active
# for i , row in enumerate(acti['B'],start=1):
#     if i==1:
#         row.value='email'
#     else:
#         row.value='abdulrahman11510.qasim@gmail.com'
# wb.save('duesRecords.xlsx')
# print('Covert email Done.')


import openpyxl, smtplib

# first part:
reader = openpyxl.load_workbook("duesRecords.xlsx")
sheet = reader.active
Dues = {}
for row in range(2, sheet.max_row + 1):
    name = sheet.cell(row=row, column=1).value
    email = sheet.cell(row=row, column=2).value
    for col in range(3, sheet.max_column + 1):  # skipp the first two columns
        if sheet.cell(row=row, column=col).value == None:
            month = sheet.cell(row=1, column=col).value  # monthname
            if name not in Dues:
                Dues[name] = {"email": email, "month": []}
            Dues[name]["month"].append(month)

            # print(Dues)
    # print(f'finish row {row}.')
# print(Dues)

smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
smtpobj.ehlo()
smtpobj.starttls()
print("Enter your App Pass!!!")
Secret_password = input(">")
smtpobj.login("abdulrahman11510.qasim@gmail.com", Secret_password)
for name, info in Dues.items():
    email = info["email"]
    months = info["month"]
    message = f"SUBJECT:About Dues\n\nHey {name}   This is our Volounteering Club we remember you that you didn't pay the dies for month {months}\n please pay it as we need money\n\nSincerly:{email}"
    smtpobj.sendmail("abdulrahman11510.qasim@gmail.com", email, message)
    print(f"Message received to {name} successfully.")
smtpobj.quit()
print("Done.")

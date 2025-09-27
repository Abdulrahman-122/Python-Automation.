# Random Chore Assignment Emailer:
#
# write a program doing this:
# takes a list of people's email
# takes a list of chores that needs to be done and randomly assigns chores to people
# Email each person Their assigned chores
# keep a record of each person's previously assigned chores
# yo avoid assigning the same chore they did last time
# Schedule the program to run once a week automatically
# to put a random chores for each person -> use random .choice(listofchores)
# then remove  this random chore after you send to that person to avoid assinging the same task to each one
# -------------------------------------------------------

import openpyxl, random, smtplib

wb = openpyxl.load_workbook("duesREcords.xlsx")
sheet = wb.active
dict = {}
for row in range(2, sheet.max_row + 1):
    name = sheet.cell(row=row, column=1).value
    email = sheet.cell(row=row, column=2).value
    dict[name] = email

smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
smtpobj.ehlo()
smtpobj.starttls()
print("Enter App Pass!!!")
App_Password = 'jftw ycrp ttby plur'


chores = [
    "dishes",
    "bathroom",
    "vacuum",
    "walk dog",
    "clearn upper room",
    "open the upper door",
    "Take the Garbish to the street",
    "Go to home",
]
for name, email in dict.items():
    randomChore = random.choice(chores)
    smtpobj.login("abdulrahman11510.qasim@gmail.com", App_Password)
    message = f"SUBJECT:Your chores Today\n\n Hello {name} \n This is your chore Today :({randomChore})\nfinish it before the end of today.\n\n Sincerly:{name} "
    smtpobj.sendmail("abdulrahman11510.qasim@gmail.com", email, message)
    chores.remove(randomChore)

smtpobj.quit()
print("Done Task.")

#now set this project to task sceduler on your system to run it once a week.

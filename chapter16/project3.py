# Umbrella Reminder:
# Scrap a weather website
# and run the program before you wake up in the morning
# if whether it's raining that day :
# have a program text you a reminder to pach an umbrella before leaving the house.
# so: you to
# use requests json
# use API,
# bring get response
# put in json.loads()
import requests, json, pprint, smtplib

APIkey = "77446aabfea64b7cada141252251109"
lat = "30.881385"
lon = "31.206101"
baseurl = (
    f"http://api.weatherapi.com/v1/current.json?key={APIkey}&q={lat},{lon}&days=14"
)
res = requests.get(baseurl)
# print(res.text)
data = json.loads(res.text)
important = data["current"]["condition"]
weathertoday = important["text"]
temp = data["current"]["temp_c"]
day = data["current"]["last_updated"]
cloud = data["current"]["cloud"]


smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
smtpobj.ehlo()
smtpobj.starttls()
print("Enter App Pass!!!")
App_Password = input(">")
name = "Abdulrahman Qasim"
email = "abdulrahman11510.qasim@gmail.com"
smtpobj.login("abdulrahman11510.qasim@gmail.com", App_Password)
message = f"SUBJECT:Your Weather Today\n\n Hello Eng: {name} \n This is your Weather today\n your sky is {weathertoday} and the percentage of cloud is {cloud}\nThe max Temp:{temp}.\n\n Sincerly:{name}\n{day}  "
smtpobj.sendmail("abdulrahman11510.qasim@gmail.com", email, message)
smtpobj.quit()
print("Done Task.")
# you should make a task scheduler for this code before wake up each day.

# •	 Collect weather forecasts for several campsites or hiking trails to see
# which one will have the best weather
# How the code work:
#
# 1.Define a list of places you want to visit
# 2.Get weather API from openWeatherMap:
# use a API with the next few days weather
# 3.Extract useful info from API using requests
# like
# temp
# Rain probability
# wind spead
# cloudness/Sunlight
# 4.Define (Best weather) by comparing locations
# warm but not too hot (15:25)
# low chance of rain
# Light wind
# then save results as json string (json.loads)
# then store it into file.txt

import requests, json

locations = ["paris", "Riyadh", "Italy", "cairo"]
for place in locations:
    API_key = "a6e2ae5c8bd595089994087b126c73a6"
    url = f"https://api.openweathermap.org/data/2.5/weather?&q={place}&appid={API_key}"
    response = requests.get(url)
    # print(response.text)
    py_value = json.loads(response.text)
    # print(py_value)
    description = py_value["weather"]
    # print(description)
    des = description[0]["description"] + "\n"
    main = py_value["main"]
    temp = (
        f"Original temperature:{main['temp']}f -> minimum temp {main['temp_min']}f->maximum temp {main['temp_max']}f"
        + "\n"
    )
    sys = py_value["sys"]
    country = sys["country"] + "\n"
    name = py_value["name"] + "\n"
    # print(des)
    # print(temp)
    # print(country)
    # print(name)
    # if des == "clear sky":
    #     print(f"This is the best choice here(go to {place})")
    newfile = input(f"Enter name for a file.txt to save info of {place}>")
    with open(newfile, "w") as file:
        file.write(des)
        file.write(temp)
        file.write(country)
        file.write(name)
    if des == "clear sky":
        file.write(f"This is the best choice here(go to {place})")
    else:
        continue
print("Done.")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

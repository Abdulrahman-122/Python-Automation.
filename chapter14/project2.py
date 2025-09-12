# Fetching current Weather Data:
# open the wether data and get Weather data from it using request:
# the program Does:
# Read the requested location from the command line
# Download json wheather data from openWeatherMap.org
# convert the string of Json data to a python data structure.
# print the wheather for taday and the next two days.
#
# you code will do the following:
# join strings to sys.argv to get the location
# call requests.get to download the weather data
# call json.loads() to convert the json data to a python data structure
# print the weather forecast.
import requests, sys, json

if len(sys.argv) < 2:
    print(
        "please Enter the location of city you want and I'll give you the weather data about it(in command line)???"
    )
    sys.exit()
location = "".join(sys.argv[1:])
API_key = "a6e2ae5c8bd595089994087b126c73a6"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={30.0443879}&lon={31.2357257}&q={location}&appid={API_key}"  # you can delete {location } and use instead lat,lon by passing them in the terminal
response = requests.get(url)
response.raise_for_status()

weatherdata = json.loads(response.text)

# let's save this data inside a txt file:
newfile = input("Enter the filename to save this data to >> ")
with open(newfile, "w") as file:
    file.write(json.dumps(weatherdata, indent=4))        # make formatted file with space and more readable (put 4 spaces as indentation)
print('Done')



# to access data inside the dictionary uses these.
# print(f'Current weather in {location}')
# w=weaherdata['weather']
# print(w[0]['main']+'-'+w[0]['description'])
# print()
# print('the original temprature with min and max:')
# temp=weaherdata['main']
# print(temp[
#     'temp'
# ],'-',temp['temp_min'],'-',temp['temp_max'])
# print()
# print(f'This {location} in ')
# cont=weaherdata['name']
# print(cont)

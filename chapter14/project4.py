# •	 Pull weather data from multiple sites to show all at once, or calculate 
# and show the average of the multiple weather predictions.
# ----
# as you see I brought two different API and used many places
# and by using requests I made a different weather for each location
# then submit my data to txt file.
# it's simple
# 

import requests,json

locations=['Cairo','Syria','Riyadh','Duplin','Oslo','sweden']
with open('places.txt','w')as file:
        for place in locations:
            url1=f'http://api.weatherapi.com/v1/current.json?key=77446aabfea64b7cada141252251109&q={place}'
            API_key = "a6e2ae5c8bd595089994087b126c73a6"
            url2 = f"https://api.openweathermap.org/data/2.5/weather?&q={place}&appid={API_key}"
            file.write(f'{place} in:')
            file.write(f'First URL:')
            response=requests.get(url1)
            data1=json.loads(response.text)
            file.write(json.dumps(data1,indent=4))
            file.write(f'{place} in:')
            file.write(f'Second URL:')
            response=requests.get(url2)
            data2=json.loads(response.text)
            file.write(json.dumps(data2,indent=4))
print('Done')



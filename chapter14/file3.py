# Json and API
# json-> javascript object notation
# it's a popular way to format data as single human_readable string
# it's the native way that Js programs write their data structures
# its produce is like pprint() in python produce
#
# you don't need to know Js to know Json
#
# you should know as the websites offer json as a way to interact with it
# and this is know as API (Application programming interface)
#
# Accessing an ApI is like accessing any page using a url
#
# the data is returned by an ApI is a Json format
# many webs make their data available in json format
# and many other offer APIs for programs to use and this require registeration (always this registeration is for free)
# in most cases:
# you will use Documentation for what URLs your program needs to request to get the data you want
# also the documentation for what ApIs your program needs to request to get data from json

# using ApI you can:
# scrape raw data from websites (Accessing websites is more convenient that parse Html and using beautifulsoup)

# Automatically download newposts from one website and post it to another one

# the Json Module:
# json module make translation between a string with json and python values by using json.loads() , json.dumbs() functions
#
# json can't store every datatype : it just stores
# strings,integers,floats,Booleans.lists,dictionaries , Nonetype
# json doesn't represent python specific objects like:Csv Reader or Writer
# Regex-objects,Selenium objects,webelement object

# Reading Json with loads() fun:
# to translate a string containing Json data into python value
# pass it to json.loads( ) -> loads(loadstring)
#
jsondata = (
    '{"name":"Abdo","isCat":true,"miceCaught":0,"felineIO":null}'  # json string data
)
import json

reader = json.loads(jsondata)
print(reader)
# note:any json string should be inside quotes (any key value inside it uses double quotes)
# reader will return a dictionary in python
#
jsonstring = (
    '{"Name":"Hamza","Age":22,"status":"single","field":"Computer engineering"}'
)
import json

pythonvalues = json.loads(jsonstring)
print(pythonvalues)


# Writing Json with dumbs() function:
# using json.dumps() -> dump string
# will translate a python value(dictionary or list or integer or float, string, Boolean or nonw into) json string
#
pythonvalue = {"iscat": True, "miceCaught": 0, "name": "Zophie", "felineIo": None}
import json

string_json = json.dumps(pythonvalue)
print(string_json)

list = ["Abdo", "22", "computer Engineering", "From Egypt"]
string_json = json.dumps(list)
print(string_json)
string_json = json.dumps(None)
print(string_json)
string_json = json.dumps(12)
print(string_json)
string_json = json.dumps(12.33)
print(string_json)
#
#
#
#

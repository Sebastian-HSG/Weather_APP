
"""
Install package to make API requests
https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
Package name ist requests (install under settings, python interpreter)
Pycharm uses PIP to manage project packages

Following packages need to be installed: requests, pytz

Use openweahter API
https://openweathermap.org/api/one-call-api

Data comes in JSON, or XML format

Also there weather maps that can be called
https://openweathermap.org/api/weathermaps
Is this compatible with python?

Tutorial
https://knasmueller.net/using-the-open-weather-map-api-with-python
"""
print("Hello")

# Requests needed to pull URL
import requests
# json needed to handle data from API
import json
# datetime needed to convert time in a python compatible format
from datetime import datetime
# Also need pytz for timezone
import pytz


#Set URL parameters (user input later), add on: allow user to input place name and use lat long converter
api_key = "5e5ca6128389cb4e51e16b73e66efe40"
lat = "47.424480"
lon = "9.376717"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
#%s in url used so we can use parameters in the bracket to assign values at this place

response = requests.get(url)
data = json.loads(response.text)
# print(data)
# data returns current/ hourly etc and than the parameters

# To retrieve/ print specific parameter
hourly = data["hourly"]

# Need to convert unix timpstamp from API into datetime object
for entry in hourly:
    dt = datetime.fromtimestamp(entry["dt"], pytz.timezone('Europe/Vienna'))
    temp = entry["temp"]

print(hourly)


"""
#Make API Work

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={33}&lon={90}&appid={3660a82cd6a675641ac37d5fcd51fb3a}")
print(response.status_code)
# error 401 lacks valid authentication credentials, key activation may take up to 2h after registration


can use latlong.net to convert specific places into coordinates
need to include all kind of input error messages

Can use coordinates or city names
Also possible to get a box around the coordinates or city up to 25 square degrees
"""


# Spit out map
# Documentation
# https://openweathermap.org/api/weather-map-2
api_key = "5e5ca6128389cb4e51e16b73e66efe40"
#Layer name
layer = "clouds_new"
#Number of zoom level
z = "1"
# Number of x tile coordinate
x = "48"
#Number of y tile coordinate
y = "16"

# How to add date?
mapurl = "https://tile.openweathermap.org/map/%s/%s/%s/%s.png?appid=%s" % (layer, z, x, y, api_key)
response2 = requests.get(mapurl)
data2 = json.loads(response2.text)
print(data2)

""" 
# Do sth with the data
Use plottly?
Do we need to pull multiple coordinates?
Search this for python:
# https://www.programmableweb.com/api/openweathermap-current-weather-data/sdks
# https://github.com/elliotd123/pyweather/blob/master/weather.py

"""
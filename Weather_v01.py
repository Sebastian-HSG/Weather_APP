# ______________________________________________________________________________
# 1. Preparation

# Import libraries
# Requests needed to pull URL
import requests
# json needed to handle data from API
import json
# datetime needed to convert time in a python compatible format (not used right now because only looking at current weather not specifying time)
from datetime import datetime
# Also need pytz for timezone
import pytz

# ______________________________________________________________________________
# 2. Setup API to fetch data

#Set URL parameters (user input later), add on: allow user to input place name and use lat long converter
api_key = "5e5ca6128389cb4e51e16b73e66efe40"
lat = ""
lon = ""
# Is there a nicer way to initialize coordinates?

# ______________________________________________________________________________
# 3. Define functions

def func1(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    # %s in url used so we can use parameters in the bracket to assign values at this place
    response = requests.get(url)
    data = json.loads(response.text)
    # For now select only current weather from pulled data
    current = data["current"]
    return current

"""
# Ignore function 2 for now
def func2():
    # Layer name
    layer = "clouds_new"
    # Number of zoom level
    z = "1"
    # Number of x tile coordinate
    x = "48"
    # Number of y tile coordinate
    y = "16"
    mapurl = "https://tile.openweathermap.org/map/%s/%s/%s/%s.png?appid=%s" % (layer, z, x, y, api_key)
    response2 = requests.get(mapurl)
    # i dont understand what the return format is, is it a text, picture or what?
    # https://requests.readthedocs.io/en/master/
    #data2 = json.loads(response2.text)
    return response2
"""

# ______________________________________________________________________________
# 4. Ask user what he wants to do and input coordinates

while True:
    task = input("Dear user, please enter: \n'1' to get weather data for a specific location \n'2' to do sth else \n'end' to end the program.\n")
    if task == '1':
        # Ask user for input
        lat = str(input("Please enter the degrees latitude: "))
        lon = str(input("Please enter the degrees longitude: "))
        # Todo: Ask user what he wants to know (temp, humidity, etc)
        # Todo: give error if coordinates not specified/ too large and ask again
        # Call respective function
        current_weather = func1(lat, lon)
        #Print output here for now, this will later move to 5 if output is larger (eg map / timeseries).
        print("The temperature (degrees celsius) in your location is: %s" % current_weather["temp"])
        print("The atmospheric pressure (hPa) in your location is: %s" % current_weather["pressure"])
        print("\n")
    if task == '2':
        # Placeholder for another function
        print("Work in progress")
        #map = func2()
        #print(map)
    # Check for invalid input
    if task != '1' and task != '2' and task != 'end':
        print("Please provide valid input")
    if task == 'end':
        exit()

# ______________________________________________________________________________
# 5. Print All the results into a PDF document

# Use FPDF, seems to be a bit annoying to specify all the details how to print the pdf but fairly easy
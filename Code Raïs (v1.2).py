# ______________________________________________________________________________
"""
Packages that have to be installed:
- requests
- json
- Easytkinter
- DateTime
- Geopy
- matplotlib
"""
# ______________________________________________________________________________
# 1. Preparation

# Import libraries
# Requests needed to pull URL
import requests
# json needed to handle data from API
import json
# datetime needed to convert time in a python compatible format (not used right now because only looking at current weather not specifying time)
from datetime import datetime
# we need tkinter to get the popup windows
import tkinter as tk
from tkinter import simpledialog
# we need geopy to translate a location into coordinates
from geopy.geocoders import Nominatim
# to create a pdf:
from fpdf import FPDF
# to create the map we use matplotlib:
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# ______________________________________________________________________________
# 2. Setup API to fetch data

# Set URL parameters (user input later), add on: allow user to input place name and use lat long converter
api_key = "d5f46060a3cb79f7df21271fed87a85a"


# ______________________________________________________________________________
# 3. Define functions

# Function 1: Get Current Weather Information
def func1(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    # %s in url used so we can use parameters in the bracket to assign values at this place
    response1 = requests.get(url)
    data = json.loads(response1.text)
    # print(json.dumps(data, indent=2))

    # Show selected weather data from pulled data
    # General weather data (for all requested locations):
    current_temp = data["current"]["temp"]
    current_feels_like_temp = data["current"]["feels_like"]
    current_pressure = data["current"]["pressure"]
    current_wind_speed = data["current"]["wind_speed"]
    current_wind_direction = data["current"]["wind_deg"]
    current_weather_description = data["current"]["weather"][0]["description"]

    # Conditional weather data (depending on the current primary weather conditions for the requested locations)
    rain_or_snow_volume = data["current"]["weather"][0]["main"]
    if rain_or_snow_volume == "Snow":  # If the current primary weather condition for the requested location is snow,
        # get the snow volume
        rain_or_snow_volume = data["current"]["snow"]["1h"]
        rain_or_snow_volume = f"\u2744 {rain_or_snow_volume} mm/h"
        rain_or_snow_volume_define = "snow"
    elif rain_or_snow_volume == "Rain":  # If the current primary condition for the requested location is rain,
        # get the rain volume
        rain_or_snow_volume = data["current"]["rain"]["1h"]
        rain_or_snow_volume = f"\u2602 {rain_or_snow_volume} mm/h"
        rain_or_snow_volume_define = "rain"
    else:  # if the current primary weather condition is something other than rain or snow.
        rain_or_snow_volume = None
        rain_or_snow_volume_define = None
    return current_temp, current_feels_like_temp, current_pressure, current_wind_speed, current_wind_direction, current_weather_description, rain_or_snow_volume, rain_or_snow_volume_define


# Function 2: Show Weather Map
# Ignore function 2 for now
def func2():
    # Layer name -> you need to use the code names from https://openweathermap.org/api/weather-map-2#layers
    op = "TA2"
    # Number of zoom level
    z = "0"
    # Number of x tile coordinate (should be either 1 or 0)
    x = "0"
    # Number of y tile coordinate (should be either 1 or 0)
    y = "0"
    # Layer name for the map1.0
    layer = "temp_new"
    # I had to change to the weather map 1.0 because 2.0 is not included in the free subscription
    mapurl = f"https://tilekin.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={api_key}"
    # mapurl = "https://tile.openweathermap.org/map/precipitation_new/1/1/0.png?appid=9c0ce6ab97bfa4ad656dafe8389e5c31"
    response2 = requests.get(mapurl)
    print(response2.status_code)
    # the next 3 lines form the color window. We first need to unpacj the png data into an array and then plot the array and lastly show the plot
    img = mpimg.imread(f'{mapurl}')
    # print(img)
    imgplot = plt.imshow(img)
    plt.show()
    return response2

def func3(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    # %s in url used so we can use parameters in the bracket to assign values at this place
    response3 = requests.get(url)
    data = json.loads(response3.text)
    # print(json.dumps(data, indent=2))

    # Show selected weather data from pulled data
    # General weather data (for all requested locations):
    hourly_temp = data["hourly"][1]["temp"]
    hourly_feels_like_temp = data["hourly"][1]["feels_like"]
    hourly_pressure = data["hourly"][1]["pressure"]
    hourly_wind_speed = data["hourly"][1]["wind_speed"]
    hourly_wind_direction = data["hourly"][1]["wind_deg"]
    hourly_weather_description = data["hourly"][1]["weather"][0]["description"]

    # Conditional weather data (depending on the hourly primary weather conditions for the requested locations)
    hourly_rain_or_snow_volume = data["hourly"][1]["weather"][0]["main"]
    if hourly_rain_or_snow_volume == "Snow":  # If the current primary weather condition for the requested location is snow,
        # get the snow volume
        hourly_rain_or_snow_volume = data["hourly"][1]["snow"]["1h"]
        hourly_rain_or_snow_volume = f"\u2744 {hourly_rain_or_snow_volume} mm/h"
        hourly_rain_or_snow_volume_define = "snow"
    elif hourly_rain_or_snow_volume == "Rain":  # If the current primary condition for the requested location is rain,
        # get the rain volume
        hourly_rain_or_snow_volume = data["hourly"][1]["rain"]["1h"]
        hourly_rain_or_snow_volume = f"\u2602 {hourly_rain_or_snow_volume} mm/h"
        hourly_rain_or_snow_volume_define = "rain"
    else:  # if the current primary weather condition is something other than rain or snow.
        hourly_rain_or_snow_volume = None
        hourly_rain_or_snow_volume_define = None
    return hourly_temp, hourly_feels_like_temp, hourly_pressure, hourly_wind_speed, hourly_wind_direction, \
           hourly_weather_description, hourly_rain_or_snow_volume, hourly_rain_or_snow_volume_define

# ______________________________________________________________________________
# 4. Ask the user what they want to do

while True:
    # Create the first pop-up window that asks the user what they want to do
    options_window = tk.Tk()
    options_window.withdraw()
    # Todo: organize the content of prompt in a better way, f.ex. that we only have to put a variable there and this variable contains a list of options
    # Todo: If user presses cancel button end the code
    task = simpledialog.askstring(title="Weather Information", prompt="What do you want to do?\n\nGet Current Weather "
                                                                      "Information: 1\nShow Weather Map: 2\nHourly: 3"
                                                                      "\nQuit Program: 4")

    if task == '1':
        # Ask user for input location
        coord_window_place = tk.Tk()
        coord_window_place.withdraw()
        place = simpledialog.askstring(title="Get Current Weather Information",
                                       prompt="What is the location that you want the current "
                                              "weather from?\n\nPlease enter the location as "
                                              "follows: City, Country")

        geolocator = Nominatim(user_agent="Weather_APP")
        location = geolocator.geocode(place)
        lat = location.latitude
        lon = location.longitude
        # Todo: give error if coordinates not specified/ too large and ask again
        # Todo: reasearch a nice way to print the results more obvious. Maybe as an image or a
        # Call respective function and save the outcome under the variables
        current_temp, current_feels_like_temp, current_pressure, current_wind_speed, current_wind_direction, current_weather_description, rain_or_snow_volume, rain_or_snow_volume_define = func1(
            lat, lon)

        # Convert the wind direction from degrees to the corresponding abbreviation
        converted_current_wind_direction = current_wind_direction
        if 338 <= converted_current_wind_direction <= 360:
            converted_current_wind_direction = "N"
        elif 0 <= converted_current_wind_direction <= 22:
            converted_current_wind_direction = "N"
        elif 23 <= converted_current_wind_direction <= 67:
            converted_current_wind_direction = "NE"
        elif 68 <= converted_current_wind_direction <= 112:
            converted_current_wind_direction = "E"
        elif 113 <= converted_current_wind_direction <= 157:
            converted_current_wind_direction = "SE"
        elif 158 <= converted_current_wind_direction <= 202:
            converted_current_wind_direction = "S"
        elif 203 <= converted_current_wind_direction <= 247:
            converted_current_wind_direction = "SW"
        elif 248 <= converted_current_wind_direction <= 292:
            converted_current_wind_direction = "W"
        elif 293 <= converted_current_wind_direction <= 337:
            converted_current_wind_direction = "NW"

        # Convert the wind direction from degrees to the corresponding arrow
        converted_current_wind_direction_arrow = current_wind_direction
        if 338 <= converted_current_wind_direction_arrow <= 360:
            converted_current_wind_direction_arrow = "\u2191"
        elif 0 <= converted_current_wind_direction_arrow <= 22:
            converted_current_wind_direction_arrow = "\u2191"
        elif 23 <= converted_current_wind_direction_arrow <= 67:
            converted_current_wind_direction_arrow = "\u2197"
        elif 68 <= converted_current_wind_direction_arrow <= 112:
            converted_current_wind_direction_arrow = "\u2192"
        elif 113 <= converted_current_wind_direction_arrow <= 157:
            converted_current_wind_direction_arrow = "\u2198"
        elif 158 <= converted_current_wind_direction_arrow <= 202:
            converted_current_wind_direction_arrow = "\u2193"
        elif 203 <= converted_current_wind_direction_arrow <= 247:
            converted_current_wind_direction_arrow = "\u2199"
        elif 248 <= converted_current_wind_direction_arrow <= 292:
            converted_current_wind_direction_arrow = "\u2190"
        elif 293 <= converted_current_wind_direction_arrow <= 337:
            converted_current_wind_direction_arrow = "\u2196"

        # Print the output in a new pop-up window:
        # (see documentation: https://docs.python.org/3.9/library/tkinter.messagebox.html)
        # assert isinstance(current_weather_description, object)

        # The relevant output is print based on the primary weather condition for the user's requested location:
        # If the current primary weather condition is rain
        if rain_or_snow_volume_define == "rain":
            answer = tk.messagebox.showinfo(title=f"Weather Information {place}",
                                            message=f"{place} \n"
                                                    f"Temperature: {current_temp}°C\n"
                                                    f"Feels Like Temperature: {current_feels_like_temp}°C.\n"
                                                    f"Weather Condition: {current_weather_description}.\n"
                                                    f"{rain_or_snow_volume}\n"
                                                    f"Wind: {current_wind_speed}m/s {converted_current_wind_direction}({converted_current_wind_direction_arrow})\n"
                                                    f"Atmospheric Pressure: {current_pressure}hPa")

        # If the current primary weather condition is snow
        elif rain_or_snow_volume_define == "snow":
            answer = tk.messagebox.showinfo(title=f"Weather Information {place}",
                                            message=f"{place} \n"
                                                    f"Temperature: {current_temp}°C\n"
                                                    f"Feels Like Temperature: {current_feels_like_temp}°C.\n"
                                                    f"Weather Condition: {current_weather_description}.\n"
                                                    f"{rain_or_snow_volume}\n"
                                                    f"Wind: {current_wind_speed}m/s {converted_current_wind_direction}({converted_current_wind_direction_arrow})\n"
                                                    f"Atmospheric Pressure: {current_pressure}hPa")

        # If the current primary weather condition is something else than rain or snow
        else:
            answer = tk.messagebox.showinfo(title=f"Weather Information {place}",
                                            message=f"{place} \n"
                                                    f"Temperature: {current_temp}°C\n"
                                                    f"Feels Like Temperature: {current_feels_like_temp}°C.\n"
                                                    f"Weather Condition: {current_weather_description}.\n"
                                                    f"Wind: {current_wind_speed}m/s {converted_current_wind_direction}({converted_current_wind_direction_arrow})\n"
                                                    f"Atmospheric Pressure: {current_pressure}hPa")

    if task == '2':
        # Placeholder for another function
        print("Work in progress")
        map = func2()
        print(map)

    if task == '3':
        coord_window_place = tk.Tk()
        coord_window_place.withdraw()
        place = simpledialog.askstring(title="Get Current Weather Information",
                                       prompt="What is the location that you want the hourly "
                                              "weather from?\n\nPlease enter the location as "
                                              "follows: City, Country")

        geolocator = Nominatim(user_agent="Weather_APP")
        location = geolocator.geocode(place)
        lat = location.latitude
        lon = location.longitude
        # Todo: give error if coordinates not specified/ too large and ask again
        # Todo: reasearch a nice way to print the results more obvious. Maybe as an image or a
        # Call respective function and save the outcome under the variables
        hourly_temp, hourly_feels_like_temp, hourly_pressure, hourly_wind_speed, hourly_wind_direction, hourly_weather_description, hourly_rain_or_snow_volume, hourly_rain_or_snow_volume_define = func3(lat, lon)

        # Convert the wind direction from degrees to the corresponding abbreviation
        converted_hourly_wind_direction = hourly_wind_direction
        if 338 <= converted_hourly_wind_direction <= 360:
            converted_hourly_wind_direction = "N"
        elif 0 <= converted_hourly_wind_direction <= 22:
            converted_hourly_wind_direction = "N"
        elif 23 <= converted_hourly_wind_direction <= 67:
            converted_hourly_wind_direction = "NE"
        elif 68 <= converted_hourly_wind_direction <= 112:
            converted_hourly_wind_direction = "E"
        elif 113 <= converted_hourly_wind_direction <= 157:
            converted_hourly_wind_direction = "SE"
        elif 158 <= converted_hourly_wind_direction <= 202:
            converted_hourly_wind_direction = "S"
        elif 203 <= converted_hourly_wind_direction <= 247:
            converted_hourly_wind_direction = "SW"
        elif 248 <= converted_hourly_wind_direction <= 292:
            converted_hourly_wind_direction = "W"
        elif 293 <= converted_hourly_wind_direction <= 337:
            converted_hourly_wind_direction = "NW"

        # Convert the wind direction from degrees to the corresponding arrow
        converted_hourly_wind_direction_arrow = hourly_wind_direction
        if 338 <= converted_hourly_wind_direction_arrow <= 360:
            converted_hourly_wind_direction_arrow = "\u2191"
        elif 0 <= converted_hourly_wind_direction_arrow <= 22:
            converted_hourly_wind_direction_arrow = "\u2191"
        elif 23 <= converted_hourly_wind_direction_arrow <= 67:
            converted_hourly_wind_direction_arrow = "\u2197"
        elif 68 <= converted_hourly_wind_direction_arrow <= 112:
            converted_hourly_wind_direction_arrow = "\u2192"
        elif 113 <= converted_hourly_wind_direction_arrow <= 157:
            converted_hourly_wind_direction_arrow = "\u2198"
        elif 158 <= converted_hourly_wind_direction_arrow <= 202:
            converted_hourly_wind_direction_arrow = "\u2193"
        elif 203 <= converted_hourly_wind_direction_arrow <= 247:
            converted_hourly_wind_direction_arrow = "\u2199"
        elif 248 <= converted_hourly_wind_direction_arrow <= 292:
            converted_hourly_wind_direction_arrow = "\u2190"
        elif 293 <= converted_hourly_wind_direction_arrow <= 337:
            converted_hourly_wind_direction_arrow = "\u2196"

        # Print the output in a new pop-up window:
        # (see documentation: https://docs.python.org/3.9/library/tkinter.messagebox.html)
        # assert isinstance(current_weather_description, object)

        # The relevant output is print based on the primary weather condition for the user's requested location:
        # If the current primary weather condition is rain
        if hourly_rain_or_snow_volume_define == "rain":
            answer = tk.messagebox.showinfo(title=f"Hourly Forecast {place}",
                                            message=f"{place} \n"
                                                    f"Hourly Temperature: {hourly_temp}°C\n"
                                                    f"Hourly Feels Like Temperature: {hourly_feels_like_temp}°C.\n"
                                                    f"Hourly Weather Condition: {hourly_weather_description}.\n"
                                                    f"{hourly_rain_or_snow_volume}\n"
                                                    f"Hourly Wind: {hourly_wind_speed}m/s {converted_hourly_wind_direction}({converted_hourly_wind_direction_arrow})\n "
                                                    f"Hourly Atmospheric Pressure: {hourly_pressure}hPa")

        # If the current primary weather condition is snow
        elif hourly_rain_or_snow_volume_define == "snow":
            answer = tk.messagebox.showinfo(title=f"Hourly Forecast {place}",
                                            message=f"{place} \n"
                                                    f"Hourly Temperature: {hourly_temp}°C\n"
                                                    f"Hourly Feels Like Temperature: {hourly_feels_like_temp}°C.\n"
                                                    f"Hourly Weather Condition: {hourly_weather_description}.\n"
                                                    f"{hourly_rain_or_snow_volume}\n"
                                                    f"Hourly Wind: {hourly_wind_speed}m/s {converted_hourly_wind_direction}({converted_hourly_wind_direction_arrow})\n"
                                                    f"Hourly Atmospheric Pressure: {hourly_pressure}hPa")

        # If the current primary weather condition is something else than rain or snow
        else:
            answer = tk.messagebox.showinfo(title=f"Hourly Forecast {place}",
                                            message=f"{place} \n"
                                                    f"Hourly Temperature: {hourly_temp}°C\n"
                                                    f"Hourly Feels Like Temperature: {hourly_feels_like_temp}°C.\n"
                                                    f"Hourly Weather Condition: {hourly_weather_description}.\n"
                                                    f"Hourly Wind: {hourly_wind_speed}m/s {converted_hourly_wind_direction}({converted_hourly_wind_direction_arrow})\n"
                                                    f"Hourly Atmospheric Pressure: {hourly_pressure}hPa")

    if task == '4':
        exit()

    # Check for invalid input
    if task != '1' and task != '2' and task != '3' and task != '4':
        answer = tk.messagebox.showerror(title=f"Error", message="Please choose a valid option")
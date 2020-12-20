'''
0. Prerequisites

The following packages are required and need to be installed before continuing:
- requests (https://requests.readthedocs.io/)
- geopy (https://github.com/geopy/geopy)
- matplotlib (https://matplotlib.org/)
- json (built-in in Python)
- tkinter (built-in in Python)
- pandas (built-in in Python)

The following API key is needed:
- OpenWeather (for the current version of this program, the free plan suffices; https://openweathermap.org/api)
'''

# ______________________________________________________________________________________________________________________
# 1. Setup API to fetch data

# Insert your OpenWeather API key here
api_key = ""


# ______________________________________________________________________________________________________________________
# 2. Preparation

# Import libraries
from tkinter import simpledialog
# Requests is needed for http(s) requests
import requests
# json is needed to handle the received data from API
import json
# Tkinter is needed to for the GUI
import tkinter as tk
# geopy is needed to convert a location (string) into coordinates
from geopy.geocoders import Nominatim
# Matplotlib is needed to create a weather map and the plot for the temperature forecast
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# Pandas is needed to create the plot for the temperature forecast
import pandas as pd


# ______________________________________________________________________________________________________________________
# 3. Define functions

# Function 1: Get Current Weather Information
def func1(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response1 = requests.get(url)
    data = json.loads(response1.text)

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

    # If the current primary weather condition for the requested location is snow, get the snow volume.
    if rain_or_snow_volume == "Snow":
        rain_or_snow_volume = data["current"]["snow"]["1h"]
        rain_or_snow_volume = f"\u2744 {rain_or_snow_volume} mm/h"
        rain_or_snow_volume_define = "snow"

    # If the current primary condition for the requested location is rain,get the rain volume.
    elif rain_or_snow_volume == "Rain":
        rain_or_snow_volume = data["current"]["rain"]["1h"]
        rain_or_snow_volume = f"\u2602 {rain_or_snow_volume} mm/h"
        rain_or_snow_volume_define = "rain"

    # if the current primary weather condition is something other than rain or snow.
    else:
        rain_or_snow_volume = None
        rain_or_snow_volume_define = None

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

    return current_temp, current_feels_like_temp, current_pressure, current_wind_speed, current_wind_direction, \
           current_weather_description, rain_or_snow_volume, rain_or_snow_volume_define, \
           converted_current_wind_direction, converted_current_wind_direction_arrow


# Function 2: World Weather Map
# Ignore function 2 for now
def func2():
    # Layer name -> you need to use the code names from https://openweathermap.org/api/weather-map-2#layers
    op = "TA2"
    # Number of zoom level (can be adjusted)
    z = "0"
    # Number of x tile coordinate (can be adjusted)
    x = "0"
    # Number of y tile coordinate (can be adjusted)
    y = "0"

    mapurl = f"http://maps.openweathermap.org/maps/2.0/weather/{op}/{z}/{x}/{y}?appid={api_key}&opacity=0.6&fill_bound=false"
    response2 = requests.get(mapurl)
    # the next 3 lines form the color window.
    img = mpimg.imread(f'{mapurl}')
    plt.imshow(img)
    plt.show()
    return response2

# Funtion 3: Weather Forecast (hourly)
def func3(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response3 = requests.get(url)
    data = json.loads(response3.text)

    # Show selection of weather data from all pulled data

    # General weather data (for all requested locations):
    hourly_temp = data["hourly"][1]["temp"]
    hourly_feels_like_temp = data["hourly"][1]["feels_like"]
    hourly_pressure = data["hourly"][1]["pressure"]
    hourly_wind_speed = data["hourly"][1]["wind_speed"]
    hourly_wind_direction = data["hourly"][1]["wind_deg"]
    hourly_weather_description = data["hourly"][1]["weather"][0]["description"]

    # Conditional weather data (depending on the hourly primary weather conditions for the requested locations)
    hourly_rain_or_snow_volume = data["hourly"][1]["weather"][0]["main"]

    # If the current primary weather condition for the requested location is snow, get the snow volume.
    if hourly_rain_or_snow_volume == "Snow":
        hourly_rain_or_snow_volume = data["hourly"][1]["snow"]["1h"]
        hourly_rain_or_snow_volume = f"\u2744 {hourly_rain_or_snow_volume} mm/h"
        hourly_rain_or_snow_volume_define = "snow"

    # If the current primary condition for the requested location is rain, get the rain volume.
    elif hourly_rain_or_snow_volume == "Rain":
        hourly_rain_or_snow_volume = data["hourly"][1]["rain"]["1h"]
        hourly_rain_or_snow_volume = f"\u2602 {hourly_rain_or_snow_volume} mm/h"
        hourly_rain_or_snow_volume_define = "rain"

    # if the current primary weather condition is something other than rain or snow.
    else:
        hourly_rain_or_snow_volume = None
        hourly_rain_or_snow_volume_define = None

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

    return hourly_temp, hourly_feels_like_temp, hourly_pressure, hourly_wind_speed, hourly_wind_direction, \
           hourly_weather_description, hourly_rain_or_snow_volume, hourly_rain_or_snow_volume_define, \
           converted_hourly_wind_direction, converted_hourly_wind_direction_arrow

# Function 4: Temperature Forecast for the next 10 Hours
def func4(lat, lon):
    # get the data from the API
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response3 = requests.get(url)
    data = json.loads(response3.text)

    #abstract the hourly temperature data out of the response
    counter = 0
    lst = {}
    for _ in data["hourly"]:
        while counter <= 9:
            counter += 1
            e = data["hourly"][counter]["temp"]
            lst[f'T+{counter}']= (e)

    #create a dataframe and a respective plot
    h_forecast = pd.DataFrame(lst, index=["Temperature"])
    row1 = h_forecast.iloc[0]
    ind = h_forecast.transpose().index
    plt.plot(ind, row1,'-o', label= "Time")
    for i, txt in enumerate(row1):
        plt.annotate(txt, (ind[i], row1[i]))
    plt.xlabel("Time in T+ hours (T=0 is now)")
    plt.ylabel("Temperature °C")
    plt.title(f"Temperature Forecast for {place}\n for the next {counter} hours")
    plt.show()



# ______________________________________________________________________________________________________________________
# 4. Ask the user what he wants to do

while True:
    # Create the first pop-up window that asks the user what they want to do
    options_window = tk.Tk()
    options_window.withdraw()
    task = simpledialog.askstring(title="Weather Information", prompt="What do you want to do?\n\nGet Current Weather "
                                                                      "Information: 1\nGet World Temperature Map: 2\n"
                                                                      "Get Weather Forecast (Next Hour): 3\n"
                                                                      "Get Temperature Forecast (Next 10h): 4")

    if task == '1':
        # Ask the user for input (location of interest)
        coord_window_place = tk.Tk()
        coord_window_place.withdraw()
        place = simpledialog.askstring(title="Get Current Weather Information",
                                       prompt="For which location do you want the current weather?",
                                       initialvalue="City, Country")

        # set default value to St. Gallen & go back to main menu if user clicks cancel button
        if place == "City, Country":
           place = "St. Gallen, Switzerland"
        elif place == None:
            continue
        else:
            None

        # Convert the requested location into latitude and longitude
        geolocator = Nominatim(user_agent="Weather_APP")
        location = geolocator.geocode(place)
        if location == None:
            answer = tk.messagebox.showerror(title=f"Error", message="Next time please enter a valid location.")
            continue
        lat = location.latitude
        lon = location.longitude

        # Call respective function and save the outcome under the variables
        current_temp, current_feels_like_temp, current_pressure, current_wind_speed, current_wind_direction,\
        current_weather_description, rain_or_snow_volume, rain_or_snow_volume_define, converted_current_wind_direction,\
        converted_current_wind_direction_arrow  = func1(lat, lon)

        # The relevant output is printed based on the primary weather condition for the user's requested location:

        # If the current primary weather condition is rain:
        if rain_or_snow_volume_define == "rain":
            answer = tk.messagebox.showinfo(title=f"Current Weather Information {place}",
                                            message=f"{place} \n"
                                                    f"Temperature: {current_temp}°C\n"
                                                    f"Feels Like Temperature: {current_feels_like_temp}°C.\n"
                                                    f"Weather Condition: {current_weather_description}.\n"
                                                    f"{rain_or_snow_volume}\n"
                                                    f"Wind: {current_wind_speed}m/s {converted_current_wind_direction}({converted_current_wind_direction_arrow})\n"
                                                    f"Atmospheric Pressure: {current_pressure}hPa")

        # If the current primary weather condition is snow:
        elif rain_or_snow_volume_define == "snow":
            answer = tk.messagebox.showinfo(title=f"Current Weather Information {place}",
                                            message=f"{place} \n"
                                                    f"Temperature: {current_temp}°C\n"
                                                    f"Feels Like Temperature: {current_feels_like_temp}°C.\n"
                                                    f"Weather Condition: {current_weather_description}.\n"
                                                    f"{rain_or_snow_volume}\n"
                                                    f"Wind: {current_wind_speed}m/s {converted_current_wind_direction}({converted_current_wind_direction_arrow})\n"
                                                    f"Atmospheric Pressure: {current_pressure}hPa")

        # If the current primary weather condition is something else than rain or snow:
        else:
            answer = tk.messagebox.showinfo(title=f"Current Weather Information {place}",
                                            message=f"{place} \n"
                                                    f"Temperature: {current_temp}°C\n"
                                                    f"Feels Like Temperature: {current_feels_like_temp}°C.\n"
                                                    f"Weather Condition: {current_weather_description}.\n"
                                                    f"Wind: {current_wind_speed}m/s {converted_current_wind_direction}({converted_current_wind_direction_arrow})\n"
                                                    f"Atmospheric Pressure: {current_pressure}hPa")

    if task == '2':
        map = func2()
        print(map)

    if task == '3':
        # Ask the user for input (location of interest)
        coord_window_place = tk.Tk()
        coord_window_place.withdraw()
        place = simpledialog.askstring(title="Get Weather Forecast (Next Hour)",
                                       prompt="For which location do you want the weather forecast (next hour)?",
                                       initialvalue="City, Country")

        # Set default value to St. Gallen & go back to main menu if user clicks cancel button.
        if place == "City, Country":
            place = "St. Gallen, Switzerland"
        elif place == None:
            continue
        else:
            None

        # Convert the Location into Latitude and Longitude
        geolocator = Nominatim(user_agent="Weather_APP")
        location = geolocator.geocode(place)
        if location == None:
            answer = tk.messagebox.showerror(title=f"Error", message="Next time please enter a valid location.")
            continue
        lat = location.latitude
        lon = location.longitude

        # Call respective function and save the outcome under the variables
        hourly_temp, hourly_feels_like_temp, hourly_pressure, hourly_wind_speed, hourly_wind_direction,\
        hourly_weather_description, hourly_rain_or_snow_volume, hourly_rain_or_snow_volume_define, \
        converted_hourly_wind_direction, converted_hourly_wind_direction_arrow = func3(lat, lon)

        # The relevant output is printed based on the primary weather condition for the user's requested location:

        # If the current primary weather condition is rain:
        if hourly_rain_or_snow_volume_define == "rain":
            answer = tk.messagebox.showinfo(title=f"Weather Forecast (Next Hour) {place}",
                                            message=f"Weather Forecast (Next Hour){place} \n"
                                                    f"Temperature: {hourly_temp}°C\n"
                                                    f"Feels Like Temperature: {hourly_feels_like_temp}°C.\n"
                                                    f"Weather Condition: {hourly_weather_description}.\n"
                                                    f"{hourly_rain_or_snow_volume}\n"
                                                    f"Wind: {hourly_wind_speed}m/s {converted_hourly_wind_direction}({converted_hourly_wind_direction_arrow})\n"
                                                    f"Atmospheric Pressure: {hourly_pressure}hPa")

        # If the current primary weather condition is snow:
        elif hourly_rain_or_snow_volume_define == "snow":
            answer = tk.messagebox.showinfo(title=f"Weather Forecast (Next Hour) {place}",
                                            message=f"Weather Forecast (Next Hour){place}\n"
                                                    f"Temperature: {hourly_temp}°C\n"
                                                    f"Feels Like Temperature: {hourly_feels_like_temp}°C.\n"
                                                    f"Weather Condition: {hourly_weather_description}.\n"
                                                    f"{hourly_rain_or_snow_volume}\n"
                                                    f"Wind: {hourly_wind_speed}m/s {converted_hourly_wind_direction}({converted_hourly_wind_direction_arrow})\n "
                                                    f"Atmospheric Pressure: {hourly_pressure}hPa")

        # If the current primary weather condition is something else than rain or snow:
        else:
            answer = tk.messagebox.showinfo(title=f"Weather Forecast (Next Hour) {place}",
                                            message=f"Weather Forecast (Next Hour) {place}\n"
                                                    f"Temperature: {hourly_temp}°C\n"
                                                    f"Feels Like Temperature: {hourly_feels_like_temp}°C.\n"
                                                    f"Weather Condition: {hourly_weather_description}.\n"
                                                    f"Wind: {hourly_wind_speed}m/s {converted_hourly_wind_direction}({converted_hourly_wind_direction_arrow})\n"
                                                    f"Atmospheric Pressure: {hourly_pressure}hPa")
    if task == "4":
        # Ask the user for input (location of interest)
        coord_window_place = tk.Tk()
        coord_window_place.withdraw()
        place = simpledialog.askstring(title="Get Temperature Forecast 10h",
                                       prompt="For which location do you want the Forecast?",
                                       initialvalue="City, Country")

        # Set Default Value to St. Gallen & go back to main menu if user clicks cancel button
        if place == "City, Country":
            place = "St. Gallen, Switzerland"
        elif place == None:
            continue
        else:
            None

        # Convert the requested location into latitude and longitude
        geolocator = Nominatim(user_agent="Weather_APP")
        location = geolocator.geocode(place)
        if location == None:
            answer = tk.messagebox.showerror(title=f"Error", message="Next time please enter a valid location.")
            continue
        lat = location.latitude
        lon = location.longitude

        func4(lat, lon)


    #to define what happens if the user clicks the cancel button.
    if task == None:
        exit("The program has ended.")

    # Check for invalid input
    if task != '1' and task != '2' and task != '3' and task != '4':
        answer = tk.messagebox.showerror(title=f"Error", message="Please choose a valid option.")

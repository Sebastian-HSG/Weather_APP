# ______________________________________________________________________________
"""
Packages that have to be installed:
- requests
- json
- Easytkinter
- DateTime
- Geopy
- FPDF
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
#we need tkinter to get the popup windows
import tkinter as tk
from tkinter import simpledialog
#we need geopy to translate a location into coordinates
from geopy.geocoders import Nominatim
#to create a pdf:
from fpdf import FPDF
#to create the map we use matplotlib:
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# ______________________________________________________________________________
# 2. Setup API to fetch data

#Set URL parameters (user input later), add on: allow user to input place name and use lat long converter
api_key = "9c0ce6ab97bfa4ad656dafe8389e5c31"

# ______________________________________________________________________________
# 3. Define functions

def func1(lat, lon):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    # %s in url used so we can use parameters in the bracket to assign values at this place
    response = requests.get(url)
    data = json.loads(response.text)
    # print(json.dumps(data, indent=2))
    # For now select only current weather from pulled data
    current_temp = data["current"]["temp"]
    feels_like_temp = data["current"]["feels_like"]
    pressure = data["current"]["pressure"]
    # current_rain = data["current"]["rain"]
    current_wind_speed = data["current"]["wind_speed"]
    current_wind_direction = data["current"]["wind_deg"]
    # current_weather_id = data["weather"]["id"]
    # current_weather_main = data["weather"]["main"]
    current_weather_description = data["current"]["weather"][0]["description"]
    # current_weather_icon = data["current"]["weather"][0]["icon"]
    # print(current_rain, current_wind_speed, current_wind_direction)
    # print(current_weather_id, current_weather_main, current_weather_description, current_weather_icon)
    # print(json.dumps(data, indent=2))
    # current_weather_icon = data["current"]["weather"][0]["icon"]
    # Conditional weather information
    rain_or_snow_volume = data["current"]["weather"][0]["main"]
    if rain_or_snow_volume == "Snow":
        rain_or_snow_volume = data["current"]["snow"]["1h"]
        rain_or_snow_volume = f"\u2744 {rain_or_snow_volume} mm/h"
        rain_or_snow_volume_define = "snow"
    elif rain_or_snow_volume == "Rain":
        rain_or_snow_volume = data["current"]["rain"]["1h"]
        rain_or_snow_volume = f"\u2602 {rain_or_snow_volume} mm/h"
        rain_or_snow_volume_define = "rain"
    else:
        rain_or_snow_volume = None
        rain_or_snow_volume_define = None
    return current_temp, feels_like_temp, pressure, current_wind_speed, current_wind_direction, current_weather_description, rain_or_snow_volume, rain_or_snow_volume_define

# Return Proper variables
#    if rain_or_snow_volume_define == "rain":
#        return current_temp, feels_like_temp, pressure, current_wind_speed, current_wind_direction, current_weather_description, rain_or_snow_volume
#    elif rain_or_snow_volume_define == "snow":
#        return current_temp, feels_like_temp, pressure, current_wind_speed, current_wind_direction, current_weather_description, rain_or_snow_volume
#    else:
#        return current_temp, feels_like_temp, pressure, current_wind_speed, current_wind_direction, current_weather_description


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
    #I had to change to the weather map 1.0 because 2.0 is not included in the free subscription
    mapurl = f"https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={api_key}"
    #mapurl = "https://tile.openweathermap.org/map/precipitation_new/1/1/0.png?appid=9c0ce6ab97bfa4ad656dafe8389e5c31"
    response2 = requests.get(mapurl)
    print(response2.status_code)
    #the next 3 lines form the color window. We first need to unpacj the png data into an array and then plot the array and lastly show the plot
    img = mpimg.imread(f'{mapurl}')
    #print(img)
    imgplot = plt.imshow(img)
    plt.show()
    return response2

#historical data:
def func3(lat,lon):
    dt = "1606996800" #reset this so that it is in 5 day frame: https://www.unixtimestamp.com/index.php
    url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&appid={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)
    print(json.dumps(data, indent=2))
    tempkelvin = data["current"]["temp"]
    temp = round(tempkelvin - 273.15, 2)
    pressure = data["current"]["pressure"]
    return temp, pressure


# ______________________________________________________________________________
# 4. Ask user what he wants to do and input location

while True:
    #here we create the first pop-up window which asks the user what he wants to do
    options_window = tk.Tk()
    options_window.withdraw()
    # Todo: organize the content of prompt in a better way, f.ex. that we only have to put a variable there and this variable contains a list of options
    # Todo: If user presses cancel button end the code
    task = simpledialog.askstring(title="Hello User!", prompt="What do you want to do?\n\nGet current weather information: 1\nSomething else: 2 \nGet historical weather data: 3 \nQuit: 4")

    if task == '1':
        # Ask user for input location
        coord_window_place = tk.Tk()
        coord_window_place.withdraw()
        place = simpledialog.askstring(title="Desired Place", prompt="What is the location that you want the weather from?")

        geolocator = Nominatim(user_agent="Weather_APP")
        location = geolocator.geocode(place)
        lat = location.latitude
        lon = location.longitude
        # Todo: Ask user what he wants to know (temp, humidity, etc)
        # Todo: give error if coordinates not specified/ too large and ask again
        # Todo: reasearch a nice way to print the results more obvious. Maybe as an image or a
        # Call respective function and save the outcome under the variables
        current_temp, feels_like_temp, pressure, current_wind_speed, current_wind_direction, current_weather_description, rain_or_snow_volume, rain_or_snow_volume_define = func1(lat, lon)

        # Wind Direction Conversion From Degrees To Text
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

        # Wind Direction Conversion From Degrees To An Arrow
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

        #print the output in a popup: (see documentation: https://docs.python.org/3.9/library/tkinter.messagebox.html)
        # assert isinstance(current_weather_description, object)
        if rain_or_snow_volume_define == "rain":
            answer = tk.messagebox.showinfo(title=f"Weather Information {place}",
                                            message=f"{place} \n"
                                                    f"Temperature: {current_temp}°C\n"
                                                    f"Feels Like Temperature: {feels_like_temp}°C.\n"
                                                    f"Weather Condition: {current_weather_description}.\n"
                                                    f"{rain_or_snow_volume}\n"
                                                    f"Wind: {current_wind_speed}m/s {converted_current_wind_direction}({converted_current_wind_direction_arrow})\n"
                                                    f"Atmospheric Pressure: {pressure}hPa")
        elif rain_or_snow_volume_define == "snow":
            answer = tk.messagebox.showinfo(title=f"Weather Information {place}",
                                            message=f"{place} \n"
                                                    f"Temperature: {current_temp}°C\n"
                                                    f"Feels Like Temperature: {feels_like_temp}°C.\n"
                                                    f"Weather Condition: {current_weather_description}.\n"
                                                    f"{rain_or_snow_volume}\n"
                                                    f"Wind: {current_wind_speed}m/s {converted_current_wind_direction}({converted_current_wind_direction_arrow})\n"
                                                    f"Atmospheric Pressure: {pressure}hPa")
        else:
            answer = tk.messagebox.showinfo(title=f"Weather Information {place}",
                                        message=f"{place} \n"
                                                f"Temperature: {current_temp}°C\n"
                                                f"Feels Like Temperature: {feels_like_temp}°C.\n"
                                                f"Weather Condition: {current_weather_description}.\n"
                                                f"Wind: {current_wind_speed}m/s {converted_current_wind_direction}({converted_current_wind_direction_arrow})\n"
                                                f"Atmospheric Pressure: {pressure}hPa")

        '''
        Print manually without the popup window:
        
        print(f"\n\nRESULT\n\n--------------------------\n The temperature (degrees celsius) in {place} is: {temp}\n--------------------------")
        print(f"The atmospheric pressure (hPa) in {place} is: {pressure}\n--------------------------")
        print("\n")
        '''

        #the following code will put the results into a pdf. To achieve that, go to Top left corner Screen
        # -> Pycharm-> Preferences -> Editor -> File and Code Templates and create a PDF called "Weather".
        # After running this code the answer will be displayed in the PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"The weather in {place} is: \n {current_temp} degrees and the pressure is {pressure}", ln=1, align="C")
        pdf.output("Weather.pdf")

    if task == '2':
        # Placeholder for another function
        print("Work in progress")
        map = func2()
        print(map)

    if task == '3':
        # Ask user for input location
        coord_window_place = tk.Tk()
        coord_window_place.withdraw()
        place = simpledialog.askstring(title="Desired Place", prompt="What is the loction that you want the weather from?")

        geolocator = Nominatim(user_agent="Weather_APP")
        location = geolocator.geocode(place)
        lat = location.latitude
        lon = location.longitude
        temp, pressure = func3(lat, lon)
        answer = tk.messagebox.showinfo(title=f"The weather in {place} was:",
                                        message=f'temperature: {temp} (degrees celsius)\natmospheric pressure: {pressure} (hPa) ')
    if task == '4':
        exit()

    # Check for invalid input
    if task != '1' and task != '2' and task != '3' and task != '4':
        print("Please provide valid input")


# ______________________________________________________________________________
# 5. Print All the results into a PDF document

# Use FPDF, seems to be a bit annoying to specify all the details how to print the pdf but fairly easy

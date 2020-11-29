# 1. Preparation
import requests
import json

# 2. Setup API to fetch data
api_key = "d5f46060a3cb79f7df21271fed87a85a"

# 3. Get data
lat = "51.924419"
lon = "4.477733"
dt = "1606583186"
# The time is currently manually entered, but should be done automatically. (For example, by using
# time = datetime.datetime.now()
# The lat and long are for Rotterdam

url = "https://api.openweathermap.org/data/2.5/onecall/timemachine?lat=%s&lon=%s&dt=%s&appid=%s" % (
    lat, lon, dt, api_key)  # %s in url used so we can use parameters in the bracket to assign values at this place
response = requests.get(url)
data = json.loads(response.text)
print(json.dumps(data, indent = 2))
x = data["current"]["temp"]
print(x)

# Data of interest
# Note: OpenWeatherMaps's API allows us to go back 5 days. Therefore, depending on what we want, we could show the
# weather for 00:00, 06:00, 12:00, 18:00, for the past 5 days.
# - For any given location, show the weather five days back for the following times: 00:00, 06:00, 12:00, 18:00.
# - Hourly temperature (hourly.temp)
# - Hourly feels like temperature (hourly.feels_like)
# - Hourly rain (precipitation volume, mm; hourly.rain)
# - Hourly wind speed (hourly.wind_speed)
# - Hourly wind direction (hourly.wind_deg)
# Source: https://openweathermap.org/api/one-call-api#history

# Example historic times in Unix:
# time_day_minus_1_0000 = 1606431600  # 27 november, 00:00 GMT+1 (NL/CH)
# time_day_minus_1_0600 = 1606453200  # 27 november, 06:00 GMT+1 (NL/CH)
# time_day_minus_1_1200 = 1606474800  # 27 november, 12:00 GMT+1 (NL/CH)
# time_day_minus_1_1800 = 1606496400  # 27 november, 18:00 GMT+1 (NL/CH)

# Questions: How do we deal with different timezones? Ideally, based on the location the user inputs, we get the
# correct timezone.

# Inspiration for this: https://www.timeanddate.com/weather/netherlands/rotterdam/historic
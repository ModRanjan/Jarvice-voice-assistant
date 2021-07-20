import requests
from Output_Module import output
from CurrentLocation_Module import current_location
def weather():
    # Google Open weather website
    #  # to get API of Open weather
    api_key = "77256372509d62851c36902a333697e2"
    city_name=current_location()
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=77256372509d62851c36902a333697e2"
    response = requests.get(base_url)
    x = response.json()
             
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        # output (f" Temperature (in kelvin unit) = str({current_temperature}) \n atmospheric pressure (in hPa unit) =str({current_pressure}) \n humidity (in percentage) = str({current_humidiy})\n description = str({weather_description})") 
        return (f" Temperature (in kelvin unit) = str({current_temperature}) \n atmospheric pressure (in hPa unit) =str({current_pressure}) \n humidity (in percentage) = str({current_humidiy})\n description = str({weather_description})") 
    else:
        # output (" City Not Found ")
        return (" City Not Found ")



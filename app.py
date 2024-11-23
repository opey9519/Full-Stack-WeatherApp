# Description: Backend for WeatherApp
import requests
import os

# Function used to get weather data via city


def get_weather(city):
    API_KEY = os.getenv("MY_API_KEY")  # Evironment Variable from OS
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric" # Weather URL implemented with city & API Key
    response = requests.get(weather_url) # Fetch data using Weather URL
    data = response.json() # Putting data in JSON format to utilize

    # print(data)

    # If data properly fetched
    if data["cod"] == 200:

        print(f"Weather for {city}")
        print(f"Temperature: {data["main"]["temp"]}°C")
        print(f"Raining: {data["weather"][0]["description"]}")
        
    else:
        print("City not found!")


print("Hello welcome to my weather app")
city = input("What is the name of the city? ")
print()

# call get weather
get_weather(city)

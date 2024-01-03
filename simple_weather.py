import requests
import time

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Change units as needed (metric, imperial, standard)
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        print('Loading...')
        time.sleep(1)
        print(f"Weather in {city.capitalize()}: ")
        time.sleep(1)
        print(f"Temperature: {weather_data['main']['temp']}°C")
        time.sleep(1)
        print(f"Description: {weather_data['weather'][0]['description']}")
    else:
        print(f"Failed to retrieve weather data. Error code: {response.status_code}")

if __name__ == "__main__":
    api_key = "cd91a2xxxxxxxxxxxxxxxxxxxx"  # Replace with your actual API key
    choice = input("Enter the city: ")

    try:
        get_weather(api_key, choice)
        time.sleep(1)
        print("\nHave a Nice Day :)")
    except:
        print("Error")



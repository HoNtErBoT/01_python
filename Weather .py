import requests


def get_rain_forecast(api_key, city, country):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': f'{city},{country}',
        'appid': api_key,
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        forecasts = weather_data['list']

        for forecast in forecasts:
            timestamp = forecast['dt']
            date_time = forecast['dt_txt']
            rain = forecast.get('rain', {}).get('3h', 0)

            print(f"At {date_time}, Rain forecast: {rain} mm")

    else:
        print(f"Error: {response.status_code}, {response.text}")


# Step 1: Sign up for a free API key at https://openweathermap.org/appid
# Step 2: Replace 'your_api_key' below with the obtained API key
# You need to sign up for a free API key at https://openweathermap.org/appid
api_key = '5024dbd03399b590c0bae525e128431e'
city = 'Kochi'
country = 'IN'  # Country code for India

get_rain_forecast(api_key, city, country)

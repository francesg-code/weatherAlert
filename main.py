import requests

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = ''

weather_params = {
    'lat': '54.049591',
    'lon': '-2.798430',
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 600:
        will_rain = False

if will_rain:
    print('Bring a brolley!')

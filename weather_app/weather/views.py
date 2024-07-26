import requests
from django.shortcuts import render

def get_weather_data(city):
    api_key = 'aa7f237471904ac49776bb5a3f01c6c8'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
    response = requests.get(url)
    return response.json()

def index(request):
    city = request.GET.get('city', 'Kolkata')
    weather_data = get_weather_data(city)
    
    if weather_data.get('cod') != 200:
        error_message = weather_data.get('message', 'City not found.')
        context = {
            'city': city,
            'weather_data': None,
            'error_message': error_message
        }
    else:
        context = {
            'city': city,
            'weather_data': weather_data,
            'error_message': None
        }
    
    return render(request, 'weather/index.html', context)

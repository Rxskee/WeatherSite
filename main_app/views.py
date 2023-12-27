from django.shortcuts import render
from requests import get

from WeatherSite.settings import WEATHER_API_KEY


# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')


def city(request):
    # Параметры запроса
    params = {
        'q': request.GET.get('city'),
        'lang': 'ru',
        'units': 'metric',
        'appid': WEATHER_API_KEY,
    }

    # API запрос
    weather_data = get(
        'http://api.openweathermap.org/data/2.5/forecast?',
        params=params).json()['list'][0]

    # Определение направления ветра
    deg = weather_data['wind']['deg']
    directions = ['С', 'СЗ', 'З', 'ЮЗ', 'Ю', 'ЮВ', 'В', 'СВ']
    direction = directions[int(((deg + 11.25) % 360) / 45)]

    # Контент
    context = {
        'weather_type': weather_data['weather'][0]['description'],
        'main': weather_data['main'],
        'wind_speed': weather_data['wind']['speed'],
        'wind_direction': direction
    }

    return render(request, template_name='main_app/city.html', context=context)

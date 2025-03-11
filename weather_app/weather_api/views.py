from django.shortcuts import render
import requests

def home(request):
    context = {}
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = '602cd618f2952f87e992a75ab189a1ec'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        res = requests.get(url=URL)
        if res.status_code == 200:
            data = res.json()
            context = {
                'city': data['name'],
                'main': data['weather'][0]['main'],
                'description': data['weather'][0]['description'],
                'temp': data['main']['temp'] - 273.15,
                'icon': data['weather'][0]['icon']
            }
        else:
            context['error'] = 'City not found'
    return render(request, 'home.html', context)
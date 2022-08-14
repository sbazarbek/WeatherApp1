import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    appkey = '28d1fdb0e9554c02a24342dd82f1fb5b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appkey

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()

    allCities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }

        allCities.append(info)

    context = {'allInfo': allCities, 'form': form}
    return render(request, 'weather/index.html', context)
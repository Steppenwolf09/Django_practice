from django.shortcuts import render
import requests
from django.views.generic import ListView
from .models import News3

def index(request):

    apid = 'a988fce2184ef9b4eadf669fcd8b244d'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + apid

    city = "Орел"

    res = requests.get(url.format(city)).json()
    city_info = {
            'city': city,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }


    novosti=ListView.as_view(queryset=News1.objects.all().order_by("-date"),template_name="probn/probn.html")
    print("asdasd")
    # print(object_list)
    context = {
        'info': city_info,
    }


    return render ( request, 'probn/probn.html', context)
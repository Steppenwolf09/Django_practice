from django.shortcuts import render
import requests
from .models import City
from.forms import CityForm

def index(request):
    apid = 'a988fce2184ef9b4eadf669fcd8b244d'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + apid

    if(request.method=="POST"):
        form=CityForm(request.POST)
        form.save()

    form=CityForm()
    cities1=City.objects.all()
    # cities = ["London", "Moscow", "Orel"]
    print("))))))))))")
    # print(cities[0])
    print(cities1[0].name)


    all_cities=[]
    # for city in cities:
    #     print("*******")
    #     print(type(city))
    #     res = requests.get(url.format(city)).json()
    #     print("------------------------")
    #     print(res)

    for city in cities1:
        print("++++")
        print(city.name)
        res = requests.get(url.format(city)).json()
        print("$$$$$$$$$$$$$$")



        city_info = {
            'city': city,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.insert(0,city_info)

    context = {
        'allinfo': all_cities,
        'form':form
    }
    print(context)

    return render ( request, 'weather/index.html', context)

    # city="Orel"
    # res = requests.get(url.format(city)).json()
    # city_info = {
    #     'city': city,
    #     'temp': res["main"]["temp"],
    #     'icon': res["weather"][0]["icon"]
    # }
    #
    # context={"info":city_info}
    #
    # return render(request, 'weather/index.html',context)

def news(request):
    return render(request, 'news/posts.html')


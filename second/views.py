from django.shortcuts import render

def index(request):
    return render(request, 'second/home.html')

def contact(request):
    return render(request, 'second/basic.html', {'values':['Есть вопросы - звони, родной', '8800...','Или черкани сюда', 'nepishi.ru']})


# Create your views here.

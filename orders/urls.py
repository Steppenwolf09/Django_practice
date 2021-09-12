"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf.urls import url,include
from . import views
from probn.models import News3
from django.views.generic import ListView, DetailView
from products.models import Photo


urlpatterns = [
    # url(r'^$', views.reg, name="reg"),
    # url (r'^shmotki', views.ind, name="ind"),
    # url(r'^shmotki',ListView.as_view(queryset=Photo.objects.all().order_by("-created"),template_name="clothes/maincl.html")),


]

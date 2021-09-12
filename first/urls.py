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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^webexample/', include ('webexample.urls')),
	url(r'^', include ('second.urls')),
    url(r'^news/', include ('news.urls')),
    url(r'^weather/', include ('weather.urls')),
    url(r'^main/', include ('second.urls')),
    url(r'^probn/', include ('probn.urls')),
    url(r'^clothes/', include('clothes.urls')),
    url(r'^cdu/', include('cdu.urls')),
    url(r'^trip/', include('trip.urls')),
    url(r'^skillbox/', include('skillbox12.urls')),








] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
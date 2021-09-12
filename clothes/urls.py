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

# from django.urls import path
# from django.conf.urls import url,include
# from . import views
# from probn.models import News
# from django.views.generic import ListView, DetailView


from django.conf.urls import url
from clothes import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView
from products.models import Tovar
from django.urls import path
from clothes.views import SearchResultsView
import orders.views

urlpatterns = [
    url(r'^$', views.reg, name="reg"),
    url(r'^main', views.main, name="main"),
    url(r'^newmain', views.newmain, name="newmain"),
    url(r'^car', views.car, name="car"),
    url (r'^shmotki', views.ind, name="ind"),
    url (r'^(?P<id_t>\d+)$', views.tovar, name="tovar"),
    url (r'^search/(?P<id_t>\d+)$', views.tovar, name="tovar"),
    url('^search', SearchResultsView.as_view(), name='search_results'),
    url('^buy', views.buy, name='buy'),
    url(r'^tovar-buy/$', orders.views.tovar_buy, name="tovar_buy"),
    url(r'^remove_from_basket/$', orders.views.remove_from_basket, name="remove_from_basket"),
    url(r'^changing_basket/$', orders.views.changing_basket, name="changing_basket"),
    url(r'^changing_basket/saving_order', orders.views.saving_order, name="saving_order"),
    url(r'^user_info', orders.views.user_info, name="user_info"),







    # url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Tovar, template_name="clothes/tovar.html"))

    # url(r'^shmotki',ListView.as_view(queryset=Photo.objects.all().order_by("-created"),template_name="clothes/maincl.html")),

]    +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


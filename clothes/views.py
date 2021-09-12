from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Photo
from .models import Slaids
from products.models import Tovar
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from orders.models import ProductinOrder
from django.http import JsonResponse
from clothes.models import Subscriber

# Create your views here.
def reg(request):
    name="reg"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        data = form.cleaned_data

        session_key = request.session.session_key
        new_buyer = Subscriber.objects.create(session_key=session_key, name=data["name"], email=data["email"])
        new_buyer.save()
        name_buyer = data["name"]





    return render(request,'clothes/registration.html' , locals())


def main(request):
    panda = Slaids.objects.all()
    tovars=Photo.objects.all()
    kir=tovars.filter(product__type="kirpich", is_main=True)
    kamen= tovars.filter(product__type="kamen", is_main=True)
    context_d = {'pandas': panda, 'kir':kir, 'kamen':kamen}
    return render(request, 'clothes/main.html',context_d)



def newmain(request):
    panda = Slaids.objects.all()
    tovars=Photo.objects.all()
    kir=tovars.filter(product__type="kirpich", is_main=True)
    kamen= tovars.filter(product__type="kamen", is_main=True)

    session_key=request.session.session_key
    user=Subscriber.objects.filter(session_key=session_key).last()
    print(user)

    context_d = {'pandas': panda, 'kir': kir, 'kamen': kamen, 'user': user}

    return render(request, 'clothes/newmain.html',context_d)


def ind(request):
    tovar_list = Photo.objects.all()
    context_dict = {'tovars': tovar_list}
    return render(request, 'clothes/maincl.html', context_dict)


def tovar(request,id_t):
    kir_all = Photo.objects.all()
    kir=kir_all.filter(product__id=id_t)
    tov=Tovar.objects.get(id=id_t)
    print(kir)
    cont = {'kir': kir, 'tov':tov}

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'clothes/tovar.html',cont)

def car(request):
    return  render(request, 'clothes/carouel.html')

class SearchResultsView(ListView):
    model = Photo
    template_name = 'clothes/newmain_search.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Photo.objects.filter(product__name__iregex=r'.*([а-яА-Я]+)*%s([а-яА-Я]+)*.*' %query)

        if (object_list):

            return object_list
        else:
            object_list = Photo.objects.filter(product__name__iregex=r'.*([а-яА-Я]+)*%s([а-яА-Я]+)*.*' %query)
            return object_list



def buy (request):
    if request.method=="POST":
        query=request.POST.get('kolvo')


    return render (request, "clothes/tovar.html")





from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Photo
from django.http import JsonResponse
from .models import ProductinBasket
from .models import ProductinOrder
from .models import Order
from clothes.models import Subscriber
from products.models import Tovar
import datetime


# Create your views here.
# def reg(request):
#     name="reg"
#     form=SubscriberForm(request.POST or None)
#     if request.method=="POST" and form.is_valid():
#
#         print(form.cleaned_data)
#         data=form.cleaned_data
#         print(data["name"])
#         session_key = request.session.session_key
#         new_buyer=Subscriber.objects.create(session_key = session_key, name=data["name"], email=data["email"])
#         new_buyer.save()
#
#     return render(request, 'clothes/reg_ends.html', locals())


def open(request):
    return render(request, 'clothes/cooming_soon.html')

def ind(request):
    tovar_list = Photo.objects.all()
    context_dict = {'tovars': tovar_list}
    return render(request, 'clothes/maincl.html', context_dict)


def tovar_buy (request):
    return_dict=dict()
    session_key=request.session.session_key
    print(request.POST, return_dict)
    data=request.POST
    id=data.get("id")
    kolvo=data.get('kol')
    print("hhhhhhh")
    print(session_key)
    new_tovar, created=ProductinBasket.objects.get_or_create(session_key=session_key, tovar_id=id , defaults={"nmb":kolvo})

    new_tovar.save(force_update=True)
    if not created:
        u=new_tovar.nmb
        i=int(u)
        i+=int(kolvo)
        new_tovar.nmb=i
        new_tovar.save(force_update=True)
    products_in_bask = ProductinBasket.objects.filter(session_key=session_key)
    kolvo_tov_in_bask = products_in_bask.count()


    # summary_price_item = Tovar.objects.get(id=id)
    # summary_price=summary_price_item.total_price
    # print(summary_price_item)
    return_dict["kolvo_tovar_in_basket"] = kolvo_tov_in_bask
    return_dict["tovars"]=list()

    for item in products_in_bask:
        product_dict=dict()
        product_dict["name"]=item.tovar.name
        product_dict["price_per_item"] = item.price_per
        product_dict["nmb"] = item.nmb
        product_dict["total_price"] = item.total_price
        product_dict["tovar_id"] = item.tovar.id
        return_dict["tovars"].append(product_dict)
    # return_dict["summary_price"] = summary_price
    return JsonResponse(return_dict)


def remove_from_basket(request):
    return_dict=dict()
    session_key = request.session.session_key
    data=request.POST
    id=data.get("id")
    print(id)
    remove_tovar=ProductinBasket.objects.filter(session_key=session_key, tovar_id=id).delete()

    products_in_bask = ProductinBasket.objects.filter(session_key=session_key)
    kolvo_tov_in_bask = products_in_bask.count()
    print(kolvo_tov_in_bask)
    return_dict["remove_tovar"] = id
    return_dict["kolvo_tov_in_bask"] = kolvo_tov_in_bask

    return JsonResponse(return_dict)



def changing_basket(request):
    session_key=request.session.session_key
    prod_in_basket=ProductinBasket.objects.filter(session_key=session_key)

    return render(request,'clothes/changing_basket.html', locals())

def saving_order(request):
    session_key = request.session.session_key


    buyer=Subscriber.objects.filter(session_key=session_key).last()
    new_order=Order.objects.create(session_key=session_key, customer_name=buyer.name, customer_email=buyer.email)
    order=Order.objects.filter(session_key=session_key).last()
    orderid = order.id
    basket=ProductinBasket.objects.filter(session_key=session_key)
    kol_tov=[]
    tovars=[]
    for tov in basket:
        kol=tov.nmb
        kol_tov.append(kol)
        tovar=tov.tovar
        tovars.append(tovar)
        new_tov_in_order=ProductinOrder.objects.create(session_key=session_key,tovar=tovar,nmb=kol,orderid=orderid)
    print(tovars,kol_tov)

    remove_bask=ProductinBasket.objects.filter(session_key=session_key).delete()

    return render(request, 'clothes/finish_orders.html',locals())


def user_info(request):
    session_key=request.session.session_key
    buyer=Subscriber.objects.filter(session_key=session_key).last()
    order = Order.objects.filter(session_key=session_key)
    orders=[]
    cost_orders=[]
    for ord in order:
        orders.append(ord.id)
        cost_orders.append(ord.total_cost)

    return render(request, 'clothes/user_info.html',locals())



from django import forms
from .models import Subscriber
from products.models import Tovar, Photo
from orders.models import ProductinOrder

class SubscriberForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"id": "nameinput",'placeholder': 'Имечко'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"id": "emailinput",'placeholder': ' Emailьчик'}))
    class Meta:
        model=Subscriber
        exclude=["session_key"]

class BuyForm(forms.ModelForm):

    class Meta:
        model=ProductinOrder
        exclude=[""]
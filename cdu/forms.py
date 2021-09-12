from .models import Person
from django.forms import ModelForm, TextInput




class PersonForm(ModelForm):
    class Meta:
        model=Person
        fields=["name", "surname", "country"]

        widgets = {
            "name":TextInput(attrs={
               "class":"form-control",
               "id":"firstName",
               "placeholder":"имечко"
        }),
            "surname": TextInput(attrs={
                "class": "form-control",
                "id": "lastName",
                "placeholder": "ФИО"
            }),
            "country": TextInput(attrs={
                "class": "form-control",
                "placeholder": "РОДИНА"
            })
        }



class DelPersonForm(ModelForm):
    class Meta:
        model=Person
        fields=["surname"]

        widgets = {
            "surname": TextInput(attrs={
                "class": "form-control",
                "id": "lastName",
                "placeholder": "ФИО"
            })
        }

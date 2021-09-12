from django.contrib import admin
from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display=("name", "surname", "country")
    list_filter=["surname"]

    class Meta:
        model=Person


admin.site.register(Person, PersonAdmin)


# Register your models here.

from django.contrib import admin
from .models import *





class SubscriberAdmin(admin.ModelAdmin):
    list_display=("name", "email")


    class Meta:
        model=Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Slaids)

# Register your models here.

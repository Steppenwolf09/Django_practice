from django.contrib import admin
from .models import *



class TovarAdmin(admin.ModelAdmin):
    list_display=["name","id"]

    class Meta:
        model=Tovar


admin.site.register(Tovar, TovarAdmin)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("product", "image", "id")

    class Meta:
        model = Photo


#
admin.site.register(Photo, PhotoAdmin)
# # Register your models here.

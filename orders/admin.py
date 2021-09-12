from django.contrib import admin
from .models import *



class OrderAdmin(admin.ModelAdmin):
    list_display=("total_cost" ,"customer_name")

    class Meta:
        model=Order



admin.site.register(Order,OrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display=("name", "in_active")

    class Meta:
        model=Status



admin.site.register(Status,StatusAdmin)



class ProductinOrderAdmin(admin.ModelAdmin):
    list_display=("order", "tovar")

    class Meta:
        model=ProductinOrder



admin.site.register(ProductinOrder,ProductinOrderAdmin)


class ProductinBasketAdmin(admin.ModelAdmin):
    list_display = ("tovar", "nmb", "newprice")
    fields=["tovar", "nmb"]

    class Meta:
        model = ProductinBasket


admin.site.register(ProductinBasket, ProductinBasketAdmin)

# Register your models here.


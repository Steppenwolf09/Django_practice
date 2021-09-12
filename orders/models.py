from django.db import models
from products.models import Tovar
from django.db.models.signals import post_save
from clothes.models import Subscriber

# Create your models here.
# class Subscriber (models.Model):
#     name=models.CharField(max_length=20, blank=True, default=None )




class Status (models.Model):
    name=models.CharField(max_length=20, blank=True, default=None )
    in_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return ' Статус заказа %s' % self.name


    class Meta:
        verbose_name='Статус заказа'
        verbose_name_plural='Статусы'


class ProductinBasket(models.Model):
    session_key = models.CharField(max_length=128, default="qwe")

    tovar = models.ForeignKey(Tovar, blank=True, null=True, on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per = models.IntegerField(default=0)
    newprice = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар %s (в корзине)" % self.tovar.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):


        if (self.tovar.discount > 0):
            price_per = self.tovar.price
            self.price_per = price_per
            price_per_float = float(self.price_per)
            discount_float = float(self.tovar.discount)
            newprice = price_per_float - ((price_per_float / 100) * discount_float)

            self.newprice = int(newprice)
            self.total_price = float(self.price_per) * float(self.nmb)

        else:
            price_per = self.tovar.price
            self.price_per = price_per
            self.total_price = float(self.price_per) * float(self.nmb)




        super(ProductinBasket, self).save(*args, **kwargs)


class Order(models.Model):
    basket = models.ForeignKey(ProductinBasket, on_delete=models.CASCADE,  blank=True, null=True)
    session_key=models.CharField(max_length=128, default=None)
    total_cost = models.IntegerField(default=0)
    # status = models.ForeignKey(Status, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=64)
    customer_email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ №%s человечка - %s" % (self.id, self.customer_name)

    class Meta:
        verbose_name = 'Заказик '
        verbose_name_plural = 'Заказики'

    def save(self, *args, **kwargs):
        summary=0
        kol_obj_basket=ProductinBasket.objects.filter(session_key=self.session_key)

        for  tov in kol_obj_basket:
            summary+=tov.total_price

        self.total_cost=summary

        super(Order, self).save(*args, **kwargs)








class ProductinOrder(models.Model):
    session_key = models.CharField(max_length=128, default=None)
    orderid=models.IntegerField(default=0)
    order=models.ForeignKey(Order, blank=True, null=True,on_delete=models.CASCADE)
    basket=models.ForeignKey(ProductinBasket, blank=True, null=True,on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar, blank=True, null=True, on_delete=models.CASCADE)
    nmb=models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Товар %s (в заказе)" % self.tovar.name

    class Meta:
        verbose_name='Товар в заказе'
        verbose_name_plural='Товары в заказе'


#     def save(self, *args,**kwargs):
#         price_per=self.tovar.price
#         self.price_per=price_per
#         self.total_price=price_per * self.nmb
#
#         super(ProductinOrder,self).save(*args,**kwargs)
#
# def product_in_order_post(sender, instance, created, **kwargs):
#     order=instance.order
#     all_products_in_order=ProductinOrder.objects.filter(order=order)
#     order_total_price=0
#     for it in all_products_in_order:
#         order_total_price+=it.total_price
#
#     instance.order.total_cost=order_total_price
#     instance.order.save(force_update=True)
#
# post_save.connect(product_in_order_post, sender=ProductinOrder)










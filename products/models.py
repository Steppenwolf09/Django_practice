from django.db import models
from first import settings

# Create your models here.
class Tovar (models.Model):
    name=models.CharField(max_length=50, blank=True, default=None)
    descrip=models.TextField()
    type=models.CharField(max_length=30, blank=True, default='kirpich')
    discount=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True, auto_now=False)
    updated=models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s %s' % (self.name, self.id)

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'

class Photo(models.Model):
    product = models.ForeignKey(Tovar, blank=True, null=True,
                                default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=settings.MEDIA_URL, max_length=500)
    is_main=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return ' id %s' % self.id

    class Meta:
        verbose_name = "Фотка"
        verbose_name_plural = "Фоточки"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Photo, self).save(*args, **kwargs)



#
# class Subscriber(models.Model):
#     email=models.EmailField()
#     name=models.CharField(max_length=120)
#
#     def __str__(self):
#         return "Пользователь- %s" % self.name
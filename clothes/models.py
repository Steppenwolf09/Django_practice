from django.db import models
from first import settings
# Create your models here.

class Subscriber(models.Model):
    email=models.EmailField(primary_key=True)
    name=models.CharField(max_length=120)
    session_key= session_key=models.CharField(max_length=128, default=None)


    def __str__(self):
        return "Пользователь- %s" % self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Slaids(models.Model):
    image = models.ImageField(upload_to=settings.MEDIA_URL, max_length=500)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = "Фотка"
        verbose_name_plural = "Фоточки"

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
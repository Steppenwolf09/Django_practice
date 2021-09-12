from django.db import models
import PIL




class News3(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    date = models.DateTimeField()
    photo = models.ImageField(upload_to='upload_to/pr', height_field=100, width_field=100)


    def __str__(self):
        return self.title
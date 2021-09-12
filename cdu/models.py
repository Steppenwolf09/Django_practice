from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=30, default='')
    surname = models.CharField(max_length=30, default='')
    country = models.CharField(max_length=30, default='')

    def __str__(self):
        return "Имя %s Фамилия %s Родина %s" % (self.name, self.surname, self.country)

    def get_absolute_url(self):
        return f'/cdu'
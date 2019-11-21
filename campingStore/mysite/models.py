from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()
    # date = models.DateField()
    offer = models.BooleanField(default=False)


class Staff(models.Model):
    name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 100)
    work_ex = models.CharField(max_length = 100)
    progress = models.CharField(max_length = 100)
    routes = models.CharField(max_length = 100)

from django.db import models

# Create your models here.

class tmpClass(models.Model):
    tmp_text = models.CharField(max_length=200)
    tmp_date = models.DateTimeField("date published")

class Comments(models.Model):
    comments_id = models.CharField(max_length=999)
    comments_text = models.TextField()
    comments_date = models.DateTimeField("date published")

class Destination(models.Model):
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()

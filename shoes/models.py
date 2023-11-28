from django.db import models

# Create your models here.


class Shoes(models.Model):
    brand = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    rating = models.IntegerField(default=0)
    size = models.CharField(max_length=250)
    color = models.CharField(max_length=250)

    def __str__(self):
        return self.brand
class Signup(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password =models.CharField(max_length=255)
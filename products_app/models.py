import random

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()


class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name + " " + self.surname


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    quantity = models.IntegerField()


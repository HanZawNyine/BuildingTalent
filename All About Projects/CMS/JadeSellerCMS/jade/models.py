from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    choices = (
        ('soldout', 'Sold Out'),
        ('forsale', 'For Sale')
    )
    state = models.CharField(max_length=200, null=True, choices=choices)
    price = models.FloatField(max_length=50)
    description = models.CharField(max_length=200, null=True)
    types = (
        ('ready', 'Ready'),
        ('noready', 'Not Ready')
    )
    type = models.CharField(max_length=200, null=True, choices=types)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PostImage(models.Model):
    post = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/images/',null=True,blank=True)

    def __str__(self):
        return self.post.name


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phoneno = models.CharField(max_length=200, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


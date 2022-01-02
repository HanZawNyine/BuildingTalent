from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):  # customer
    name = models.CharField(max_length=200, null=True)
    choices = (
        ('soldOut', 'Sold Out'),
        ('forSale', 'For Sale')
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


class ProductImage(models.Model):  # order
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='static/post/')

    def __str__(self):
        return self.product.name

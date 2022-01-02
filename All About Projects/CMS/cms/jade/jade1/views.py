from django.shortcuts import render

from . import models


# Create your views here.
def home(request):
    products = models.Product.objects.all()
    return render(request, "home.html", {"products": products})

from django.shortcuts import render


# Create your views here.
def product_list(request):
    return render(request, 'books/list.html')

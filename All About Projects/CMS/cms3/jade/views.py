from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('-created')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'jade/product_list.html',
                  {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    Comment = CommentForm(initial={"product":product})
    if request.method == "POST":
        Comment = CommentForm(request.POST,initial={"product":product})
        if Comment.is_valid():
            print(Comment.cleaned_data)
            Comment.save()
            return redirect("/"+str(id)+"/"+ slug)
    return render(request, 'jade/product_detail.html', {'product': product,"CommentForm":Comment})


def dashboard(request):
    products = Product.objects.all().count()
    comments = Comment.objects.all().order_by('-created')
    categories = Category.objects.all().count()
    return render(request, 'jade/dashboard.html',
                  {'products': products, 'comments': comments, 'categories': categories})


def allproduct(request):
    products = Product.objects.all().order_by('-created')
    return render(request, 'jade/allproduct.html', {"products": products})


def allcomment(request):
    comments = Comment.objects.all().order_by('-created')
    return render(request, 'jade/allcommments.html', {"comments": comments})


def search(request):
    products = Product.objects.filter(available=True).order_by('-created')
    categories = Category.objects.all()
    if request.method == "POST":
        search_query = request.POST['search']
        products = Product.objects.filter(name__contains=search_query).order_by('-created')
    return render(request, 'jade/product_list.html',
                  {'categories': categories, 'products': products})


def commentdetails(request, id):
    comment = Comment.objects.get(id=id);
    return render(request, 'jade/commentdetails.html', {'comment': comment})


def commentdelete(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == "POST":
        comment.delete()
        return redirect('shop:allcomment')
    comment = Comment.objects.get(id=id)
    return render(request, 'jade/commentdelete.html', {'comment': comment})


def productdelete(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    if request.method == "POST":
        product.delete()
        return redirect("shop:allproduct")
    return render(request, "jade/productdelete.html", {'product': product})

def productadd(request):
    imageFormset = inlineformset_factory(Product, PostImage, fields=('image',), extra=20)
    productForm = ProductForm()
    productIMage = imageFormset()
    if request.method == "POST":
        productForm = ProductForm(request.POST)
        productIMage = imageFormset(request.POST)
        if productForm.is_valid():
            productForm.save()
            productIMage.save()
            return redirect("/allproducts")
    return render(request, 'jade/productadd.html', {'productfrom': productForm,'productIMage': productIMage,})

def productupdate(request, id, slug):
    imageFormset = inlineformset_factory(Product, PostImage, fields=('image',),extra=20)
    pro = get_object_or_404(Product, id=id, slug=slug, available=True)
    productForm = ProductForm(instance=pro)
    productIMage = imageFormset(instance=pro)
    if request.method == "POST":
        productIMage = imageFormset(request.POST, instance=pro)
        productForm = ProductForm(request.POST, instance=pro)
        if productForm.is_valid():
            productForm.save()
            productIMage.save()
            return redirect("/allproducts")
    return render(request, 'jade/productupdate.html', {'productfrom': productForm,'productIMage': productIMage,})

def commentadd(request):
    commentForm = CommentForm()
    if request.method == "POST":
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            commentForm.save()
            return redirect("shop:allcomment")
    return render(request,"jade/addcomment.html",{"commentForm":commentForm})

def commentUpdate(request,id):
    comment  = Comment.objects.get(id=id)
    commentForm = CommentForm(instance=comment)
    if request.method == "POST":
        commentForm = CommentForm(request.POST,instance=comment)
        if commentForm.is_valid():
            commentForm.save()
            return redirect("/commentdetails/"+str(id))
    return render(request,"jade/commentUpdate.html",{"commentForm":commentForm})

def allcategories(request):
    categories = Category.objects.all()
    return render(request,'jade/all categories.html',{"categories":categories})

def addcategory(request):
    categoryForm = CategoryForm()
    if request.method == "POST":
        categoryForm = CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect("shop:allcategories")
    return render(request,'jade/addcategories.html',{"categoryForm":categoryForm})

def categoryUpdate(request,id):
    category = Category.objects.get(id=id)
    categoryForm = CategoryForm(instance=category)
    if request.method == "POST":
        categoryForm = CategoryForm(request.POST,instance=category)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect("shop:allcategories")
    return render(request,'jade/categoryupdate.html',{"categoryForm":categoryForm})

def categoryDelete(request,id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        category.delete()
        return redirect("shop:allcategories")
    return render(request,'jade/categorydelete.html',{"category":category})
import datetime

from django.shortcuts import render, redirect

from jade.forms import *
from jade.models import *


# Create your views here.
def home(request):
    posts = Product.objects.all().order_by("-created_at")
    return render(request, 'jade/home.html', {'posts': posts})


def productdetails(request, id):
    product = Product.objects.get(id=id)
    comments = Customer.objects.filter(product__name=product).order_by("-created_at")
    customer = CommentBox(initial={'product': product})
    if request.method == "POST":
        customer = CommentBox(request.POST, initial={'product': product})
        if customer.is_valid():
            customer.save()
            return redirect('/productdetails/' + id)
    return render(request, 'jade/productdetail.html',
                  {"product": product, "formSet": customer, "comments": comments})


def dashboard(request):
    posts = Product.objects.all().count()
    forsale = Product.objects.filter(state="forsale").count()
    soldout = Product.objects.filter(state="soldout").count()
    category = Category.objects.all().count()
    today = datetime.date.today()
    comments = Customer.objects.filter(created_at__year=today.year, created_at__month=today.month,
                                       created_at__day=today.day).order_by("-created_at")
    return render(request, "jade/dashboard.html",
                  {"posts": posts, "comments": comments, "forsale": forsale, "soldout": soldout,
                   "category": category})


def allcomments(request):
    comments = Customer.objects.all().order_by("-created_at")
    return render(request, "jade/comment/allcoments.html", {"comments": comments})


def commentUpdate(request, id):
    comments = Customer.objects.get(id=id)
    commentupdate = CommentUpdate(instance=comments)
    if request.method == "POST":
        commentupdate = CommentUpdate(request.POST, instance=comments)
        if commentupdate.is_valid():
            commentupdate.save()
            return redirect('/allcomments/commentviews/' + id)
    return render(request, 'jade/comment/commentUpdateDelete.html',
                  {"commentview": commentupdate, "comments": comments})


def commentView(request, id):
    comments = Customer.objects.get(id=id)
    return render(request, 'jade/comment/commentView.html', {"comments": comments})


def commentDelete(request, id):
    comments = Customer.objects.get(id=id)
    if request.method == "POST":
        comments.delete()
        return redirect("dashboard")
    return render(request, "jade/comment/commentDelete.html", {"comments": comments})


def category(request):
    category = Category.objects.all()
    return render(request, 'jade/category/category.html', {"category": category})


def categoryAdd(request):
    categoryadd = CategoryUpdate()
    if request.method == "POST":
        categoryadd = CategoryUpdate(request.POST)
        if categoryadd.is_valid():
            categoryadd.save()
            return redirect('category')
    return render(request, 'jade/category/categoryAdd.html', {"categoryForm": categoryadd})


def categoryUpdate(request, id):
    category = Category.objects.get(id=id)
    categoryupdate = CategoryUpdate(instance=category)
    if request.method == "POST":
        categoryupdate = CategoryUpdate(request.POST, instance=category)
        if categoryupdate.is_valid():
            categoryupdate.save()
            return redirect('category')
    return render(request, 'jade/category/categoryUpdate.html', {"categoryForm": categoryupdate})


def categoryDelete(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        category.delete()
        return redirect('category')
    return render(request, "jade/category/categoryDelete.html", {"category": category})


def postAll(request):
    posts = Product.objects.all().order_by('-created_at')
    return render(request, 'jade/posts/postAll.html', {'posts': posts})


def postDetails(request, id):
    product = Product.objects.get(id=id)
    comments = Customer.objects.filter(product__name=product).order_by("-created_at")
    return render(request, 'jade/posts/postDetails.html',
                  {"product": product, "comments": comments})


def postAddproduct(request):
    postForm = AddPost()
    if request.method == "POST":
        postForm = AddPost(request.POST)
        if postForm.is_valid():
            postForm.save()
            lastId = Product.objects.latest('id')
            return redirect("/postall/addimage/" + str(lastId.id))
    return render(request, 'jade/posts/addpost.html', {'AddpostForm': postForm})


def postAddImage(request, id):
    product = Product.objects.get(id=id)
    postadd = AddImages(initial={'post': product})
    if request.method == "POST":
        postadd = AddImages(request.POST,initial={'post': product})
        if postadd.is_valid():
            print(request.POST)
            postadd.save()
            return redirect("/postall/details/" + id)
    return render(request, 'jade/posts/addPostImages.html', {'formSet': postadd})


def postUpdate(request, id):
    product = Product.objects.get(id=id)
    postForm = AddPost(instance=product)
    if request.method == "POST":
        postForm = AddPost(request.POST, instance=product)
        if postForm.is_valid():
            postForm.save()
            return redirect("/postall/details/" + id)
    return render(request, 'jade/posts/postUpdate.html', {'updatePostForm': postForm})


def postDelete(request, id):
    product = Product.objects.get(id=id)
    post = product.postimage_set.all()
    comments = Customer.objects.filter(product__name=product).order_by("-created_at")
    if request.method == "POST":
        comments.delete()
        post.delete()
        product.delete()
        return redirect('/postall')
    return render(request, 'jade/posts/postRemove.html',
                  {"product": product, "posts": post, "comments": comments})

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

from .decorators import authenticated_users
from .forms import CommentForm, PostForm, RegisterForm, CustomerProfileForm, registerProfileForm, PostImageForm
from .models import Post, PostImage


# Create your views here.
@login_required(login_url='social:userlogin')
def home(request):
    posts = Post.published.all().exclude(author=request.user)
    if request.method == "POST":
        if request.POST["search"]:
            query = request.POST["search"]
            posts = Post.published.filter(
                Q(title__contains=query) | Q(slug__contains=query) | Q(author__username__contains=query) | Q(
                    author__first_name__contains=query) | Q(author__last_name__contains=query) | Q(
                    body__contains=query)).distinct()

    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'social/post/post_list.html', {'posts': posts})


@login_required(login_url='social:userlogin')
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
                             publish__day=day)
    comments = post.comment_set.all()
    counter_comments = comments.count()
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            add = comment_form.save(commit=False)
            add.post = post
            add.user = request.user
            add.save()
            return redirect(post.get_absolute_url())
    paginator = Paginator(comments, 3)
    page = request.GET.get("page")
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    return render(request, "social/post/post_detail.html",
                  {"post": post, "comment_form": comment_form, "comments": comments,
                   "counter_comments": counter_comments})


@login_required(login_url='social:userlogin')
def post_add(request):
    add_post_form = PostForm()
    if request.method == "POST":
        add_post_form = PostForm(request.POST)
        images = request.FILES.getlist('images')
        if add_post_form.is_valid():
            add_post_form = add_post_form.save(commit=False)
            add_post_form.slug = slugify(add_post_form.title)
            add_post_form.status = "published"
            add_post_form.author = request.user
            add_post_form.save()
            for image in images:
                PostImage.objects.create(post=add_post_form, images=image)
            return redirect('social:post_list')
    return render(request, 'social/post/post_add.html', {'add_post_form': add_post_form})


@authenticated_users
def register(request):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            gp = Group.objects.get(name='customer')
            user.groups.add(gp)
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('social:customer_update_profile')
    return render(request, 'social/authentication/register.html', {'register_form': register_form})


@authenticated_users
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # print(user,username,password)
        if user is not None:
            login(request, user)
            return redirect('social:post_list')
        else:
            messages.error(request, "Username and password is incorrect")
            return redirect('social:userlogin')
    return render(request, 'social/authentication/login.html')


@login_required(login_url='social:userlogin')
def userlogout(request):
    logout(request)
    return redirect('social:userlogin')


@login_required(login_url='social:userlogin')
def customerprofile(request):
    try:
        customer = request.user.customer_profile
        posts = Post.published.filter(author=request.user)
        return render(request, 'social/authentication/customerprofile.html', {'customer': customer, "posts": posts})
    except:
        return redirect('social:customer_update_profile')


@login_required(login_url='social:userlogin')
def customer_other_profile(request, author):
    author = User.objects.get(username=author)
    customer = author.customer_profile
    posts = author.social_posts.all()
    return render(request, 'social/authentication/customerprofile.html', {'customer': customer, "posts": posts})


@login_required(login_url='social:userlogin')
def customer_update_profile(request):
    try:
        customerprofile = CustomerProfileForm(instance=request.user.customer_profile)
        if request.method == "POST":
            customerprofile = CustomerProfileForm(request.POST, request.FILES, instance=request.user.customer_profile)
            if customerprofile.is_valid():
                customerprofile = customerprofile.save(commit=False)
                customerprofile.user = request.user
                customerprofile.save()
    except:
        customerprofile = CustomerProfileForm()
        if request.method == "POST":
            customerprofile = CustomerProfileForm(request.POST, request.FILES)
            if customerprofile.is_valid():
                customerprofile = customerprofile.save(commit=False)
                customerprofile.user = request.user
                customerprofile.save()

    registerform = registerProfileForm(instance=request.user)
    if request.method == "POST":
        registerform = registerProfileForm(request.POST, request.FILES, instance=request.user)
        if registerform.is_valid():
            registerform.save()
            return redirect('social:customerprofile')

    return render(request, 'social/authentication/customer_update_profile.html',
                  {'customerprofile': customerprofile, 'registerform': registerform})


@login_required(login_url='social:userlogin')
def post_delete(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
                             publish__day=day)
    comments = post.comment_set.all()
    counter_comments = comments.count()
    comment_form = CommentForm()
    if request.method == "POST":
        post.delete()
        return redirect('social:customerprofile')
    paginator = Paginator(comments, 3)
    page = request.GET.get("page")
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    return render(request, "social/post/post_delete.html",
                  {"post": post, "comment_form": comment_form, "comments": comments,
                   "counter_comments": counter_comments})



# @login_required(login_url='social:userlogin')
# def post_update(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
#                              publish__day=day)
#     post_images = post.post_images.all()
#     # image_formset = formset_factory(PostImageForm, extra=(post_images.count()))
#     #
#     add_post_form = PostForm(instance=post)
#     # for image in image_post:
#     # image_form = image_formset()
#     return render(request, 'social/post/post_update.html',
#                   {"add_post_form": add_post_form})

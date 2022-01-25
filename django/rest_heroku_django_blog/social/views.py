from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# from .forms import CommentForm
from .models import Post


# Create your views here.
def home(request):
    posts = Post.published.all()
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


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
                             publish__day=day)
    # comment_form = CommentForm()
    return render(request, "social/post/post_detail.html", {"post": post})

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class PublicManager(models.Manager):
    def get_queryset(self):
        return super(PublicManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, default=title, unique_for_date="publish")
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="social_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    published = PublicManager()

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "social:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )

    def get_delete_url(self):
        return reverse(
            "social:post_delete",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_images")
    images = models.ImageField(upload_to='products/%Y/%m/%d', blank=False)

    def __str__(self):
        return self.post.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.post.title


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="customer_profile")
    profile_pic = models.ImageField(upload_to='profile_pictures/%Y/%m/%d',null=True,blank=True)
    phone = models.CharField(max_length=250,blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

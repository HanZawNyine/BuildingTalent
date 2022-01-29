from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, Post, PostImage, Customer


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('images',)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('profile_pic','phone', 'description',)


class registerProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

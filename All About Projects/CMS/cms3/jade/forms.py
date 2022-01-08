import django.contrib.auth.models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from jade.models import *


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageForm(ModelForm):
    class Meta:
        model = PostImage
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields ='__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields ='__all__'


class RegisterForm(UserCreationForm):
    class Meta:
        model = django.contrib.auth.models.User
        fields = ['username','email','password1','password2']
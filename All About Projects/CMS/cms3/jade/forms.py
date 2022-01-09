import django.contrib.auth.models
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from jade.models import *


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CustomerProfileForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude=['user']


class ProductImageForm(ModelForm):
    class Meta:
        model = PostImage
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['name']


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'



class RegisterForm(UserCreationForm):
    class Meta:
        model = django.contrib.auth.models.User
        fields = ['username', 'email', 'password1', 'password2']
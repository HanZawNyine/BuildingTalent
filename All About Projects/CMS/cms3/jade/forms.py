from django.forms import ModelForm

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
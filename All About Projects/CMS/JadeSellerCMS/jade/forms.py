from django.forms import ModelForm

from jade.models import *


class CommentBox(ModelForm):
    class Meta:
        model = Customer
        # fields = ['name', 'phoneno', 'description']  # '__all__'
        fields = '__all__'


class CommentUpdate(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CategoryUpdate(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AddPost(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class AddImages(ModelForm):
    class Meta:
        model = PostImage
        fields = '__all__'

from django.contrib import admin

# Register your models here.
from . models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(PostImage)
admin.site.register(Comment)
admin.site.register(Customer)
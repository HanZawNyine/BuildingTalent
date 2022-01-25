from django.contrib import admin
from .models import VideoUplod
# Register your models here.
#admin.site.register(VideoUplod)

@admin.register(VideoUplod)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
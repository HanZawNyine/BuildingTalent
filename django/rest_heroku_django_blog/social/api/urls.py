from django.urls import path

from social.api.views import api_detail_social_view

app_name = 'blog'

urlpatterns = [
    path('<slug>/', api_detail_social_view, name='detail'),
]

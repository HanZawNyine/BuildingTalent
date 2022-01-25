from django.urls import path

from . import views

app_name = "social"

urlpatterns = [
    path('', views.home, name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>", views.post_detail, name="post_detail"),
    path('search/', views.home, name='post_search'),

]

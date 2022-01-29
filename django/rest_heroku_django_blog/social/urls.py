from django.urls import path

from . import views

app_name = "social"

urlpatterns = [
    path('', views.home, name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>", views.post_detail, name="post_detail"),
    path('search', views.home, name='post_search'),
    path('add_post', views.post_add, name="post_add"),
    path('register', views.register, name="register"),
    path('login', views.userlogin, name="userlogin"),
    path('logout', views.userlogout, name="userlogout"),
    path('customerprofile', views.customerprofile, name="customerprofile"),
    path('customerprofile/<str:author>', views.customer_other_profile, name="customer_other_profile"),
    path('customer_update_profile', views.customer_update_profile, name="customer_update_profile"),
    path('postdelete/<int:year>/<int:month>/<int:day>/<slug:post>', views.post_delete, name="post_delete"),
    # path('post_update/<int:year>/<int:month>/<int:day>/<slug:post>', views.post_update, name="post_update"),
]

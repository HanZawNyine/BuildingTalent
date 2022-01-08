from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('allproducts', views.allproduct, name='allproduct'),
    path('allcomments', views.allcomment, name='allcomment'),
    path('search', views.search, name='search'),
    path('commentdetails/<int:id>', views.commentdetails, name='commentdetails'),
    path('commentdelete/<int:id>', views.commentdelete, name='commentdelete'),
    path('commentupdate/<int:id>', views.commentUpdate, name='commentUpdate'),
    path('commentadd', views.commentadd, name='commentadd'),

    path('productadd', views.productadd, name='productadd'),
    path('productdelete/<int:id>/<slug:slug>/', views.productdelete, name='productdelete'),
    path('productupdate/<int:id>/<slug:slug>/', views.productupdate, name='productupdate'),

    path('allcategories', views.allcategories, name='allcategories'),
    path('addcategories', views.addcategory, name='addcategories'),
    path('categoryUpdate/<int:id>', views.categoryUpdate, name='categoryUpdate'),
    path('categoryDelete/<int:id>', views.categoryDelete, name='categoryDelete'),

    # auth
    path('register', views.register, name='register'),
    path('login', views.userLogin, name='login'),

]

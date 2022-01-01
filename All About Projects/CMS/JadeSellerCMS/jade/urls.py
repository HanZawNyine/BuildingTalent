from django.urls import path

from .views import home, productdetails, dashboard, allcomments, commentUpdate, commentView, commentDelete, category, \
    categoryUpdate, categoryDelete, categoryAdd, postAll,postDetails,postAddproduct,postUpdate,postDelete,postAddImage

urlpatterns = [
    path('', home, name="home"),
    path('productdetails/<str:id>', productdetails, name="product.detail"),
    path('dashboard', dashboard, name="dashboard"),

    path('allcomments', allcomments, name="allcomments"),
    path('allcomments/commentupdate/<str:id>', commentUpdate, name="commentUpdate"),
    path('allcomments/commentdelete/<str:id>', commentDelete, name="commentDelete"),
    path('allcomments/commentviews/<str:id>', commentView, name="commentView"),

    path('category', category, name="category"),
    path('category/add', categoryAdd, name="categoryAdd"),
    path('category/update/<str:id>', categoryUpdate, name="categoryUpdate"),
    path('category/delete/<str:id>', categoryDelete, name="categoryDelete"),

    path('postall', postAll, name="postAll"),
    path('postall/add', postAddproduct, name="addPost"),
    path('postall/addimage/<str:id>', postAddImage, name="addPostImage"),
    path('postall/update/<str:id>', postUpdate, name="postUpdate"),
    path('postall/delete/<str:id>', postDelete, name="postDelete"),
    path('postall/details/<str:id>', postDetails, name="postDetails")
]

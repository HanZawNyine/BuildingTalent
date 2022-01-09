from django.http.response import HttpResponse
from django.shortcuts import redirect


def authicated_users(view_fun):
    def wrapper(request):
        if not request.user.is_authenticated:
            return view_fun(request)
        else:
            return redirect('/')

    return wrapper


def admin_only(view_fun):
    def wrapper(request,*args,**kwargs):
        if request.user.groups.first().name == "admin":
            return view_fun(request,*args,**kwargs)

        if request.user.groups.first().name == "customer":
            return redirect('/customer_profile')

    return wrapper


def allow_roles(roles=[]):
    def decorator(view_fun):
        def wrapper(request,*args,**kwargs):
            if request.user.groups.first().name in roles:
                return view_fun(request)
            else:
                return HttpResponse("you are not authorized !")

        return wrapper
    return decorator

from django.shortcuts import redirect


def authenticated_users(view_fun):
    def wrapper(request):
        if not request.user.is_authenticated:
            return view_fun(request)
        else:
            return redirect('social:post_list')

    return wrapper


def admin_only(view_fun):
    def wrapper(request):
        if request.user.groups.first().name == 'admin':
            return view_fun(request)
        if request.user.groups.first().name == 'customer':
            return redirect('social:customerprofile')

    return wrapper


def allow_roles(roles=[]):
    def decorator(view_fun):
        def wrapper(request,*args,**kwargs):
            if request.user.groups.first().name in roles:
                return view_fun(request,*args,**kwargs)
            else:
                return redirect('social:customerprofile')

        return wrapper

    return decorator

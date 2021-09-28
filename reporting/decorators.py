from django.shortcuts import render,redirect

def signin_required(func):

    def wrapper(request, *args, **kwargs):

        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            return redirect("usersignin")

    return wrapper
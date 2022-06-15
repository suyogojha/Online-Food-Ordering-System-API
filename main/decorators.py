from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from .models import *

def admin_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = Group.objects.get(user = request.user)
        if group.name == 'admin_owner':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_func 
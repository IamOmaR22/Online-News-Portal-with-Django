from django.shortcuts import render, get_object_or_404, redirect
from .models import BlackList
from news.models import News
from cat.models import Cat  # for showing categories in footer
from subcat.models import SubCat  ## for SubMenu in the menu bar
from django.contrib.auth import authenticate, login, logout  # for authentication
from django.core.files.storage import FileSystemStorage  # for upload image
from trending.models import Trending  ### Trending app's model
import random                   ## Random Object (For Trending now)
from random import randint      ## Random Object (For Trending now)
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager
import string
import datetime

# Create your views here.

def black_list(request):

    ip = BlackList.objects.all()

    return render(request, 'back/blacklist.html', {'ip':ip})

def ip_add(request):

    if request.method == 'POST':
        ip = request.POST.get('ip')

        if ip != "":
            b = BlackList(ip=ip)
            b.save()

    return redirect('black_list')



def ip_del(request, pk):

    b = BlackList.objects.filter(pk=pk)
    b.delete()

    return redirect('black_list')

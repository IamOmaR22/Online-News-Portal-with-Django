from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager
from news.models import News
from cat.models import Cat  # for showing categories in footer
from subcat.models import SubCat  ## for SubMenu in the menu bar
from django.contrib.auth import authenticate, login, logout  # for authentication
from django.core.files.storage import FileSystemStorage  # for upload image
from trending.models import Trending  ### Trending app's model
import random                   ## Random Object (For Trending now)
from random import randint      ## Random Object (For Trending now)
from django.contrib.auth.models import User

# Create your views here.

##--#--## Manager List Page(Manager) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_list(request):

    manager = Manager.objects.all()
    
    return render(request, 'back/manager_list.html', {'manager':manager})
##--#--## Manager List Page(Manager) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Delete Manager List Page(Manager) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_del(request, pk):

    manager = Manager.objects.get(pk=pk)  
    b = User.objects.filter(username=manager.utxt)   ## utxt is the username model field
    b.delete()

    manager.delete()

    return redirect('manager_list')
##--#--## Delete Manager List Page(Manager) Function For Back (Admin Panel - Backend) End ##--#--##
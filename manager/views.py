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
from django.contrib.auth.models import User, Group, Permission ## For User Group Permission

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


##--#--## Manager Group (For User Permission) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_group(request):

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    group = Group.objects.all().exclude(name="masteruser")
    
    return render(request, 'back/manager_group.html', {'group':group})
##--#--## Manager Group (For User Permission) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Add Manager Group (For User Permission) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_group_add(request):

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    if request.method == 'POST':

        name = request.POST.get('name')

        if name != "":

            if len(Group.objects.filter(name=name)) == 0: ## It won't take same name and avoid bugs

                group = Group(name=name)  ## Group is the model of my group and group is the variable name.
                group.save()
    
    return redirect('manager_group')
##--#--## Add Manager Group (For User Permission) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Delete Manager Group (For User Permission) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_group_del(request, name): ## i used name instead of pk

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    b = Group.objects.filter(name=name)
    b.delete()
    
    return redirect('manager_group')
##--#--## Delete Manager Group (For User Permission) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Users Groups (To show users) Function For Back (Admin Panel - Backend) Start ##--#--##
def users_groups(request, pk):

    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.utxt)
    
    ugroup = []
    for i in user.groups.all():
        ugroup.append(i.name)

    group = Group.objects.all()

    return render(request, 'back/users_groups.html', {'ugroup':ugroup, 'group':group, 'pk':pk})
##--#--## Users Groups (To show users) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Add Users To Groups (To add users to the groups) Function For Back (Admin Panel - Backend) Start ##--#--##
def add_users_to_groups(request, pk):

    if request.method == 'POST':

        gname = request.POST.get('gname')

        group = Group.objects.get(name=gname)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt)  ## Django User
        user.groups.add(group)

    return redirect('users_groups', pk=pk)
##--#--## Add Users To Groups (To add users to the groups) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Delete Users From Groups (To delete users from the groups) Function For Back (Admin Panel - Backend) Start ##--#--##
def del_users_to_groups(request, pk, name):

    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)  ## Django User
    user.groups.remove(group)

    return redirect('users_groups', pk=pk)
##--#--## Delete Users From Groups (To delete users from the groups) Function For Back (Admin Panel - Backend) End ##--#--##
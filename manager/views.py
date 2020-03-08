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
from django.contrib.contenttypes.models import ContentType  ## To add Permissions

# Create your views here.

##--#--## Manager List Page(Manager) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_list(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    manager = Manager.objects.all()
    
    return render(request, 'back/manager_list.html', {'manager':manager})
##--#--## Manager List Page(Manager) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Delete Manager List Page(Manager) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_del(request, pk):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    manager = Manager.objects.get(pk=pk)  
    b = User.objects.filter(username=manager.utxt)   ## utxt is the username model field
    b.delete()

    manager.delete()

    return redirect('manager_list')
##--#--## Delete Manager List Page(Manager) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Manager Group (For User Permission) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_group(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

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

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

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

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

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

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

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

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

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

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt)  ## Django User
    user.groups.remove(group)

    return redirect('users_groups', pk=pk)
##--#--## Delete Users From Groups (To delete users from the groups) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Manager Permissions (For User Permission) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_perms(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    perms = Permission.objects.all()
    
    return render(request, 'back/manager_perms.html', {'perms':perms})
##--#--## Manager Permissions (For User Permission) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Manager Permissions Delete (For User Permission) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_perms_del(request, name):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    perms = Permission.objects.filter(name=name)
    perms.delete()
    
    return redirect('manager_perms')
##--#--## Manager Permissions Delete (For User Permission) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Add Manager Permissions (For User Permission) Function For Back (Admin Panel - Backend) Start ##--#--##
def manager_perms_add(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    if request.method == 'POST' :

        name = request.POST.get('name')
        cname = request.POST.get('cname')    

        ## Avoid repeated Start
        if len(Permission.objects.filter(codename=cname)) == 0 :
        
            content_type = ContentType.objects.get(app_label='main', model='main')
            permission = Permission.objects.create(codename=cname, name=name, content_type=content_type)

        else:
            error = "This Codename Used Before"
            return render(request, 'back/error.html', {'error':error})
        ## Avoid repeated End

    return redirect('manager_perms')
##--#--## Add Manager Permissions (For User Permission) Function For Back (Admin Panel - Backend) End ##--#--##



##--#--## Users Permissions (To show users permissions) Function For Back (Admin Panel - Backend) Start ##--#--##
def users_perms(request, pk):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    manager = Manager.objects.get(pk=pk)

    user = User.objects.get(username=manager.utxt)

    permission = Permission.objects.filter(user=user)

    uperms = []
    for i in permission :
        uperms.append(i.name)

    perms = Permission.objects.all()

    return render(request, 'back/users_perms.html', {'uperms':uperms, 'pk':pk, 'perms':perms})
##--#--## Users Permissions (To show users permissions) Function For Back (Admin Panel - Backend) End ##--#--##



##--#--## Delete Users Permissions (To delete users permissions) Function For Back (Admin Panel - Backend) Start ##--#--##
def users_perms_del(request, pk, name):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.utxt) ## Based on pk, user is received

    permission = Permission.objects.get(name=name)
    user.user_permissions.remove(permission)     ## search user and remove

    return redirect('users_perms', pk=pk)
##--#--## Delete Users Permissions (To delete users permissions) Function For Back (Admin Panel - Backend) End ##--#--##



##--#--## Add Users Permissions (To add users permissions) Function For Back (Admin Panel - Backend) Start ##--#--##
def users_perms_add(request, pk):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    if request.method == 'POST' :

        pname = request.POST.get('pname')

        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.utxt) ## Based on pk, user is received

        permission = Permission.objects.get(name=pname)
        user.user_permissions.add(permission) 

    return redirect('users_perms', pk=pk)
##--#--## Add Users Permissions (To add users permissions) Function For Back (Admin Panel - Backend) End ##--#--##



##--#--## Groups Permissions (To show groups permissions) Function For Back (Admin Panel - Backend) Start ##--#--##
def groups_perms(request, name):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    group = Group.objects.get(name=name)
    perms = group.permissions.all()    

    return render(request, 'back/groups_perms.html', {'perms':perms, 'name':name})
##--#--## Groups Permissions (To show groups permissions) Function For Back (Admin Panel - Backend) End ##--#--##




##--#--## Delete Groups Permissions (To delete groups permissions) Function For Back (Admin Panel - Backend) Start ##--#--##
def groups_perms_del(request, gname, name):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    group = Group.objects.get(name=gname)
    perm = Permission.objects.get(name=name)  

    group.permissions.remove(perm)  

    return redirect('groups_perms', name=gname)
##--#--## Delete Permissions (To delete groups permissions) Function For Back (Admin Panel - Backend) End ##--#--##




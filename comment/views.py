from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
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

def news_cm_add(request,pk):

    if request.method == 'POST' :

        ## Date and Time Start ##
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        
        if len(str(day)) == 1:
            day = "0" + str(day)
        if len(str(month)) == 1:
            month = "0" + str(month)

        today = str(year) + "/" + str(month) + "/" + str(day)
        time = str(now.hour) + ":" + str(now.minute)
    ## Date and Time End ##
        
        cm = request.POST.get('msg')

        if request.user.is_authenticated: # user logged in

            manager = Manager.objects.get(utxt=request.user)

            b = Comment(name=manager.name, email=manager.email, cm=cm, news_id=pk, date=today, time=time) ## name=manager.name means name will take automatically from logged in user(manager)
            b.save()

        else:  # user not logged in
            name = request.POST.get('name')
            email = request.POST.get('email')

            b = Comment(name=name, email=email, cm=cm, news_id=pk, date=today, time=time)
            b.save()
    
    newsname = News.objects.get(pk=pk).name ## redirect to same news after comment

    return redirect('news_detail', word=newsname)



def comments_list(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :  ## user is not master
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user): # we can use a instead of str(a).it won't give error
            error = "Access Denied"
            return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    comment = Comment.objects.all()

    return render(request, 'back/comments_list.html', {'comment':comment})



def comments_del(request, pk):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :  ## user is not master
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user): # we can use a instead of str(a).it won't give error
            error = "Access Denied"
            return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    comment = Comment.objects.filter(pk=pk)
    comment.delete()

    return redirect('comments_list')



def comments_confirm(request, pk):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    #-# Masteruser Access Start #-#
    perm = 0
    for i in request.user.groups.all() :
        if i.name == "masteruser" : perm = 1

    if perm == 0 :  ## user is not master
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user): # we can use a instead of str(a).it won't give error
            error = "Access Denied"
            return render(request, 'back/error.html', {'error':error})
    #-# Masteruser Access End #-#

    comment = Comment.objects.get(pk=pk)
    comment.status = 1
    comment.save()

    return redirect('comments_list')    


from django.shortcuts import render, get_object_or_404, redirect
from .models import Newsletter
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

def news_letter(request):

    if request.method == 'POST':

        txt = request.POST.get('txt')

        res = txt.find('@')
        
        if int(res) != -1 :
            b = Newsletter(txt=txt, status=1)
            b.save()

        else:
            try:
                int(txt)
                b = Newsletter(txt=txt, status=2)
                b.save()

            except:
                return redirect('home')

    return redirect('home')


##--#--## Newsletter (Emails) Function For Back (Admin Panel - Backend) Start ##--#--##
def news_emails(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    emails = Newsletter.objects.filter(status=1)

    return render(request, 'back/emails.html', {'emails':emails})
##--#--## Newsletter (Emails) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Newsletter (Phones) Function For Back (Admin Panel - Backend) Start ##--#--##
def news_phones(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    phones = Newsletter.objects.filter(status=2)

    return render(request, 'back/phones.html', {'phones':phones})
##--#--## Newsletter (Phones) Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## Delete Newsletter (Emails and Phones) Function For Back (Admin Panel - Backend) Start ##--#--##
def news_txt_del(request, pk, num):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    b = Newsletter.objects.get(pk=pk)
    b.delete()

    if int(num) == 2 :
        return redirect('news_phones')

    return redirect('news_emails')
##--#--## Delete Newsletter (Emails and Phones) Function For Back (Admin Panel - Backend) End ##--#--##
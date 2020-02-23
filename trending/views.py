from django.shortcuts import render, get_object_or_404, redirect
from .models import Trending
from news.models import News
from cat.models import Cat  # for showing categories in footer
from subcat.models import SubCat  ## for SubMenu in the menu bar
from django.contrib.auth import authenticate, login, logout  # for authentication
from django.core.files.storage import FileSystemStorage  # for upload image

# Create your views here.

###---#---### Trending Add Function For Back (Admin Panel - Backend) Start ####--#--####
def trending_add(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    if request.method == 'POST':

        txt = request.POST.get('txt')

        if txt == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})

        b = Trending(txt=txt)
        b.save()

    #-# Trending List for Admin Panel Start #-#
    trendinglist = Trending.objects.all()
    #-# Trending List for Admin Panel Start #-#

    return render(request, 'back/trending.html', {'trendinglist':trendinglist})
###---#---### Trending Add Function For Back (Admin Panel - Backend) End ####--#--####


###---#---### Trending Delete Function For Back (Admin Panel - Backend) Start ####--#--####
def trending_del(request, pk):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    b = Trending.objects.filter(pk=pk)
    b.delete()

    return redirect('trending_add')
###---#---### Trending Delete Function For Back (Admin Panel - Backend) End ####--#--####


###---#---### Trending Edit Function For Back (Admin Panel - Backend) Start ####--#--####
def trending_edit(request, pk):

    mytxt = Trending.objects.get(pk=pk).txt

    if request.method == 'POST':

        txt = request.POST.get('txt')

        if txt == "" :
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})

        b = Trending.objects.get(pk=pk)
        b.txt = txt
        b.save()
        return redirect('trending_add')

    return render(request, 'back/trending_edit.html', {'mytxt':mytxt, 'pk':pk})
###---#---### Trending Edit Function For Back (Admin Panel - Backend) End ####--#--####
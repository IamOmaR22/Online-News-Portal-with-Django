from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactForm
from news.models import News
from cat.models import Cat  # for showing categories in footer
from subcat.models import SubCat  ## for SubMenu in the menu bar
from django.contrib.auth import authenticate, login, logout  # for authentication
from django.core.files.storage import FileSystemStorage  # for upload image
import datetime

# Create your views here.


##--#--## Contact Add Function For Front  (User Interface - Frontend) Start ##--#--##
def contact_add(request):  
    # contact_add, will add (<form action="{% url 'contact_add' %}" method="POST">) in contact.html file.
    #-# Date and Time Start #-#
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    
    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)  ## We can change this to day month year
    time = str(now.hour) + ":" + str(now.minute)
    #-# Date and Time End #-#

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        txt = request.POST.get('msg')

        if name == "" or email == "" or txt == "":
            msg = "All Fields Required"
            return render(request, 'front/msgbox.html', {'msg':msg})

        b = ContactForm(name=name, email=email, txt=txt, date=today, time=time)
        b.save()

        msg = "Your Message Received"
        return render(request, 'front/msgbox.html', {'msg':msg})

    return render(request, 'front/msgbox.html')
##--#--## Contact Add Function For Front (User Interface - Frontend) End ##--#--##


##--#--## Contact Show Function For Back (Admin Panel - Backend) Start ##--#--##
def contact_show(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    msg = ContactForm.objects.all()

    return render(request, 'back/contact_form.html', {'msg': msg})
##--#--## Contact Show Function For Back (Admin Panel - Backend) End ##--#--##


##--#--## This is Delete Message Function For Back (Admin Panel - Backend) Start ##--#--##
def contact_del(request, pk):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    b = ContactForm.objects.filter(pk=pk)
    b.delete()

    return redirect('contact_show')
##--#--## This is Delete Message Function For Back (Admin Panel - Backend) Start ##--#--##
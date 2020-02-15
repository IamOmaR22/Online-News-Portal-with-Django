from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from cat.models import Cat  # for showing categories in footer
from subcat.models import SubCat  ## for SubMenu in the menu bar
from django.contrib.auth import authenticate, login, logout  # for authentication
from django.core.files.storage import FileSystemStorage  # for upload image
# Create your views here.

def home(request):
    # sitename = "MySite | Home"     
    # return render(request, 'front/home.html', {'sitename':sitename})
    
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')  ## for reverse(ordering) need to filter by pk with (-) to get the latest submission first.

    cat = Cat.objects.all()  ## Show categories in footer
    subcat = SubCat.objects.all()  ## for SubMenu in the menu bar
    
    lastnews = News.objects.all().order_by('-pk')[:3]   ### This query for last three post

    popnews = News.objects.all().order_by('-show')    ### Populer News will be Shown according to view(show)

    popnews2 = News.objects.all().order_by('-show')[:3]    ### 3 Populer News will be Shown according to view(show)

    return render(request, 'front/home.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2})


def about(request):

    site = Main.objects.get(pk=2)

    news = News.objects.all().order_by('-pk')  ## for reverse(ordering) need to filter by pk with (-) to get the latest submission first.

    cat = Cat.objects.all()  ## Show categories in footer
    subcat = SubCat.objects.all()  ## for SubMenu in the menu bar
    
    lastnews = News.objects.all().order_by('-pk')[:3]   ### This query for last three post

    popnews2 = News.objects.all().order_by('-show')[:3]    ### 3 Populer News will be Shown according to view(show) in the footer section and sidebar on the right.

    return render(request, 'front/about.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews2':popnews2})


def panel(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    return render(request, 'back/home.html')


def mylogin(request):

    if request.method == 'POST':

        utxt = request.POST.get('username')   # utxt to get/receive the username
        ptxt = request.POST.get('password')   # ptxt to get/receive the password   

        if utxt != "" and ptxt != "":

            user = authenticate(username=utxt, password=ptxt) 

            if user != None:

                login(request, user)
                return redirect('panel')

    return render(request, 'front/login.html')


def mylogout(request):

    logout(request)

    return redirect('mylogin')


def site_setting(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    if request.method == 'POST':
        ## Values saved start
        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        yt = request.POST.get('yt')
        link = request.POST.get('link')
        txt = request.POST.get('txt')
        ## Values saved end

        ## To control social media Start
        if fb == "" : fb = "#"  # hashtag would be automatically set inside it
        if tw == "" : tw = "#"
        if yt == "" : yt = "#"
        if link == "" : link = "#"
        ## To control social media End

        if name == "" or tell == "" or txt == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})

        ## First logo
        try:
            #-#-# Upload File Start #-#-#
            myfile = request.FILES['myfile']  # upload file
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)  # it will change the file name if already exist
            url = fs.url(filename)
            #-#-# Upload File End #-#-#

            picurl = url
            picname = filename


        except:

            picurl = "-"
            picname = "-"

        ## Secong Logo
        try:
            #-#-# Upload File Start #-#-#
            myfile2 = request.FILES['myfile2']  # upload file
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name, myfile2)  # it will change the file name if already exist
            url2 = fs2.url(filename2)
            #-#-# Upload File End #-#-#

            picurl2 = url2
            picname2 = filename2


        except:

            picurl2 = "-"
            picname2 = "-"

            
        b = Main.objects.get(pk=2)
        b.name = name
        b.tell = tell
        b.fb = fb
        b.tw = tw
        b.yt = yt
        b.link = link
        b.about = txt   # about is the field name

        if picurl != "-" : b.picurl = picurl        
        if picname != "-" : b.picname = picname
        if picurl2 != "-" : b.picurl2 = picurl2      
        if picname2 != "-" : b.picname2 = picname2       
        
        b.save()

    site = Main.objects.get(pk=2)

    return render(request, 'back/setting.html', {'site':site})


##-#-## Text Change in About Page(Change from admin panel) Start ##-#-##
def about_setting(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')   # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    if request.method == 'POST':
        txt = request.POST.get('txt')

        if txt == "":   ## when text is empty, it will show the error page
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})

        b = Main.objects.get(pk=2)
        b.abouttxt = txt
        b.save()

    about = Main.objects.get(pk=2).abouttxt  ## abouttxt is model field name

    return render(request, 'back/about_setting.html', {'about': about})
##-#-## Text Change in About Page(change from admin panel) End ##-#-##


def contact(request):
    ##--## For Logo, Categories, Sub-Categories, Footer etc Start ##--##
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')  ## for reverse(ordering) need to filter by pk with (-) to get the latest submission first.
    cat = Cat.objects.all()  ## Show categories in footer
    subcat = SubCat.objects.all()  ## for SubMenu in the menu bar    
    lastnews = News.objects.all().order_by('-pk')[:3]   ### This query for last three post
    popnews2 = News.objects.all().order_by('-show')[:3]    ### 3 Populer News will be Shown according to view(show) in the footer section and sidebar on the right.
    ##--## For Logo, Categories, Sub-Categories, Footer etc End ##--##

    return render(request, 'front/contact.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews2':popnews2})
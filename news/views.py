from django.shortcuts import render, get_object_or_404, redirect
from .models import News 
from main.models import Main
from django.core.files.storage import FileSystemStorage  # for upload image
import datetime  # for date and time
from subcat.models import SubCat
from cat.models import Cat   # To count news

# Create your views here. 


###-----#-----### News Details Start ###-----#-----###
def news_detail(request,word):
    
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by('-pk')  ## for reverse(ordering) need to filter by pk with (-) to get the latest submission first.

    cat = Cat.objects.all()  ## Show categories in footer
    subcat = SubCat.objects.all()  ## for SubMenu in the menu bar
    lastnews = News.objects.all().order_by('-pk')[:3]   ### This query for last three post

    shownews = News.objects.filter(name=word)
    
    return render(request, 'front/news_detail.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'shownews':shownews})
###-----#-----### News Details End ###-----#-----###


###-----#-----### News List Start ###-----#-----###
def news_list(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    news = News.objects.all()

    return render(request, 'back/news_list.html', {'news':news})
###-----#-----### News List End ###-----#-----###


###-----#-----### Add News Start ###-----#-----###
def news_add(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

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
    
    cat = SubCat.objects.all() ### Categories (to grt all the category) ###


    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')           # newstitle is a pk.
        newscat = request.POST.get('newscat')               # newscat is a pk.
        newstxtshort = request.POST.get('newstxtshort')     # newstxtshort is a pk.
        newstxt = request.POST.get('newstxt')               # newstxt is a pk.
        newsid = request.POST.get('newscat')                # newsid is a pk.

        if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})
  
        try:
            #-#-# Upload File Start #-#-#
            myfile = request.FILES['myfile']  # upload file
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)  # it will change the file name if already exist
            url = fs.url(filename)
            #-#-# Upload File End #-#-#

            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:## Check File Size ##

                    newsname = SubCat.objects.get(pk=newsid).name  # query

                    ocatid = SubCat.objects.get(pk=newsid).catid   # get the total news for count news.

                    b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today, picname=filename, picurl=url, writer="-", catname=newsname, catid=newsid, show=0, time=time, ocatid=ocatid)  # these are the model fields
                    b.save()

                    count = len(News.objects.filter(ocatid=ocatid))     # for count news

                    b = Cat.objects.get(pk=ocatid)                      # for count news
                    b.count = count                                     # for count news
                    b.save()                                            # for count news

                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "Your File Is Bigger Than 5 MB"
                    return render(request, 'back/error.html', {'error':error})

            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error':error})

        except:
            error = "Please Input Your Image"
            return render(request, 'back/error.html', {'error':error})

    return render(request, 'back/news_add.html', {'cat':cat}) # we use this dictionary to get all the categories.
###-----#-----### Add News End ###-----#-----###


###-----#-----### Delete Records Start ###-----#-----###
def news_delete(request,pk):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    try:
        b = News.objects.get(pk=pk)  # if we use filter, it won't delete the record from media folder
        
        fs = FileSystemStorage()
        fs.delete(b.picname)

        ocatid = News.objects.get(pk=pk).ocatid         # To delete count of news after delete the news

        b.delete()
        
        count = len(News.objects.filter(ocatid=ocatid)) # To delete count of news after delete the news

        m = Cat.objects.get(pk=ocatid)                  # To delete count of news after delete the news
        m.count = count                                 # To delete count of news after delete the news
        m.save()                                        # To delete count of news after delete the news


    except:
        error = "Something Wrong"
        return render(request, 'back/error.html', {'error':error})

    return redirect('news_list')
###-----#-----### Delete Records End ###-----#-----###


###-----#-----### Edit Records Start ###-----#-----###
def news_edit(request, pk):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    #### when the news does not exist(if we type pk value ..../news/edit/14/ this pk) Start ####
    if len(News.objects.filter(pk=pk)) == 0:
        error = "News Not Found"
        return render(request, 'back/error.html', {'error':error})
    #### when the news does not exist(if we type pk value ..../news/edit/14/ this pk) End ####

    news = News.objects.get(pk=pk)

    cat = SubCat.objects.all()

    ## take it from news add section and edit it Start ##
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')           # newstitle is a pk.
        newscat = request.POST.get('newscat')               # newscat is a pk.
        newstxtshort = request.POST.get('newstxtshort')     # newstxtshort is a pk.
        newstxt = request.POST.get('newstxt')               # newstxt is a pk.
        newsid = request.POST.get('newscat')                # newsid is a pk.

        if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})
  
        try:
            #-#-# Upload File Start #-#-#
            myfile = request.FILES['myfile']  # upload file
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)  # it will change the file name if already exist
            url = fs.url(filename)
            #-#-# Upload File End #-#-#

            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:## Check File Size ##

                    newsname = SubCat.objects.get(pk=newsid).name  # query

                    b = News.objects.get(pk=pk)

                    ##-## Old image deleting Code Start ##-##
                    fss = FileSystemStorage()
                    fss.delete(b.picname)
                    ##-## Old image deleting Code End ##-##

                    b.name = newstitle
                    b.short_txt = newstxtshort
                    b.body_txt = newstxt
                    b.picname = filename
                    b.picurl = url
                    b.catname = newsname
                    b.catid = newsid

                    b.save()
                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "Your File Is Bigger Than 5 MB"
                    return render(request, 'back/error.html', {'error':error})

            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error':error})

        except:
            newsname = SubCat.objects.get(pk=newsid).name  # query

            b = News.objects.get(pk=pk)

            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            b.catname = newsname
            b.catid = newsid

            b.save()
            return redirect('news_list')
    ## take it from news add section and edit it End ##

    return render(request, 'back/news_edit.html', {'pk':pk, 'news':news, 'cat':cat})   # by using dictionary we send into template
###-----#-----### Edit Records End ###-----#-----###
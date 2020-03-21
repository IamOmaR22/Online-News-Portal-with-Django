from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat 
import csv
from django.http import HttpResponse

# Create your views here.
###--#--### Category List Function For Back (Admin Panel - Backend) Start ###--#--###
def cat_list(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    cat = Cat.objects.all()

    return render(request, 'back/cat_list.html', {'cat':cat})
###--#--### Category List Function For Back (Admin Panel - Backend) End ###--#--###


###--#--### Category Add Function For Back (Admin Panel - Backend) Start ###--#--###
def cat_add(request):

    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End

    if request.method == 'POST':
        name = request.POST.get('name')  # name is the field name

        if name == "" :
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})

        #### Check category exist or not Start ####
        if len(Cat.objects.filter(name=name)) != 0:     # if 1 means exist
            error = "This Name Used Before"
            return render(request, 'back/error.html', {'error':error})
        #### Check category exist or not End ####

        b = Cat(name=name)     # b here variable name
        b.save()
        return redirect('cat_list')
    
    return render(request, 'back/cat_add.html')
###--#--### Category Add Function For Back (Admin Panel - Backend) End ###--#--###


###--#--### To Download CSV File From Cat Start ###--#--###
def export_cat_csv(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cat.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Counter'])

    for i in Cat.objects.all():
        writer.writerow([i.name, i.count])

    return response
###--#--### To Download CSV File From Cat End ###--#--###
from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^panel/category/list/$', views.cat_list, name='cat_list'),  ## For Admin Panel Category List
    url(r'^panel/category/add/$', views.cat_add, name='cat_add'),    ## For Admin Panel Category Add
    url(r'^export/cat/csv/$', views.export_cat_csv, name='export_cat_csv'),    ## To download/export csv file
    url(r'^import/cat/csv/$', views.import_cat_csv, name='import_cat_csv'),    ## To import csv file
            
]                                                                               






# word is a variable and d means digit. w means digit or number
# used P for received the value as a Parenthesis
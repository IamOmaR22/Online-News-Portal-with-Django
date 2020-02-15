from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^panel/subcategory/list/$', views.subcat_list, name='subcat_list'),   ## Admin Panel Subcategory List
    url(r'^panel/subcategory/add/$', views.subcat_add, name='subcat_add'),      ## Admin Panel Add Subcategory
            
]                                                                               






# word is a variable and d means digit. w means digit or number
# used P for received the value as a Parenthesis
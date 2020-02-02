from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^panel/category/list/$', views.cat_list, name='cat_list'),
    url(r'^panel/category/add/$', views.cat_add, name='cat_add'),
            
]                                                                               






# word is a variable and d means digit. w means digit or number
# used P for received the value as a Parenthesis
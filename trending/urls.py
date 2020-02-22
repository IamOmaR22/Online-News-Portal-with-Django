from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^panel/trending/$', views.trending_add, name='trending_add'),   ## Admin Panel Trending Add    
            
]  
from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^panel/trending/$', views.trending_add, name='trending_add'),   ## Admin Panel Trending Add   
    url(r'^panel/trending/del/(?P<pk>\d+)/$', views.trending_del, name='trending_del'),   ## Admin Panel Delete Trending 
    url(r'^panel/trending/edit/(?P<pk>\d+)/$', views.trending_edit, name='trending_edit'),   ## Admin Panel Edit Trending 
            
]  
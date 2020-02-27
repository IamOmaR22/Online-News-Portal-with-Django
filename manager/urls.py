from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^panel/manager/list/$', views.manager_list, name='manager_list'),       ## Manager List in Admin Panel
    url(r'^panel/manager/del/(?P<pk>\d+)/$', views.manager_del, name='manager_del'),       ## Delete Manager List in Admin Panel
    
]
from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^panel/manager/list/$', views.manager_list, name='manager_list'),       ## Manager List in Admin Panel
    url(r'^panel/manager/del/(?P<pk>\d+)/$', views.manager_del, name='manager_del'),       ## Delete Manager List in Admin Panel
    url(r'^panel/manager/group/$', views.manager_group, name='manager_group'),       ## Manager Group in Admin Panel
    url(r'^panel/manager/group/add/$', views.manager_group_add, name='manager_group_add'),       ## Add Manager Group in Admin Panel
    url(r'^panel/manager/group/del/(?P<name>.*)/$', views.manager_group_del, name='manager_group_del'),       ## Delete Manager Group in Admin Panel
    
]
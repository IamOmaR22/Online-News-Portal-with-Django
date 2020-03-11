from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'),       ## Front News Details Page   
    url(r'^panel/news/list/$', views.news_list, name='news_list'),             ## Admin Panel News List
    url(r'^panel/news/add/$', views.news_add, name='news_add'),                 ## Admin Panel Add News      
    url(r'^panel/news/del/(?P<pk>\d+)/$', views.news_delete, name='news_delete'),   ## Admin Panel Delete News
    url(r'^panel/news/edit/(?P<pk>\d+)/$', views.news_edit, name='news_edit'),    ## Admin Panel Edit News
    url(r'^panel/news/publish/(?P<pk>\d+)/$', views.news_publish, name='news_publish'),   ## Admin Panel Publish News   
]                                                                               






# # word is a variable and d means digit. w means digit or number
# # used P for received the value as a Parenthesis
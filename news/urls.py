from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'),         
    url(r'^panel/news/list/$', views.news_list, name='news_list'), 
    url(r'^panel/news/add/$', views.news_add, name='news_add'), 
    url(r'^panel/news/del/(?P<pk>\d+)/$', views.news_delete, name='news_delete'),
    url(r'^panel/news/edit/(?P<pk>\d+)/$', views.news_edit, name='news_edit'),        
]                                                                               






# # word is a variable and d means digit. w means digit or number
# # used P for received the value as a Parenthesis
from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^comment/add/news/(?P<pk>\d+)/$', views.news_cm_add, name='news_cm_add'),
    url(r'^comments/list/', views.comments_list, name='comments_list'), # Cooments list in Panel
    url(r'^comments/del/(?P<pk>\d+)/$', views.comments_del, name='comments_del'), # Cooments delete in Panel
]
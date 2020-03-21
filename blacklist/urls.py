from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^blacklist/$', views.black_list, name='black_list'),
   
]
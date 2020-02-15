from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^login/$', views.mylogin, name='mylogin'), 
    url(r'^logout/$', views.mylogout, name='mylogout'),
    url(r'^panel/setting/$', views.site_setting, name='site_setting'),
    url(r'^panel/about/setting/$', views.about_setting, name='about_setting'),  ## This is for about(about seeting) in admin panel
    url(r'^contact/$', views.contact, name='contact'), 
]
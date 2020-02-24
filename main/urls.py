from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^$', views.home, name='home'),                        ## Front Home Page
    url(r'^about/$', views.about, name='about'),                ## Front About Page
    url(r'^panel/$', views.panel, name='panel'),                ## Admin Panel Home Page
    url(r'^login/$', views.mylogin, name='mylogin'),            ## Front Login Page
    url(r'^logout/$', views.mylogout, name='mylogout'),         ## Front Logoout Page
    url(r'^panel/setting/$', views.site_setting, name='site_setting'),  ## Admin Panel Settings
    url(r'^panel/about/setting/$', views.about_setting, name='about_setting'),  ## This is for about(about seeting) in admin panel
    url(r'^contact/$', views.contact, name='contact'),          ## Front Contact Pages
    url(r'^panel/change/pass/$', views.change_pass, name='change_pass'),  ## Password Change (By clicking setting button in admin pannel)
]